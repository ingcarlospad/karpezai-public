"""«Conversar»: the owner's parameters and the reference end-of-turn rule (M23-02, M23-03, M23-05; D365–D368).

«Conversar» is page behaviour (D364): the chat page listens after the owner's tap, closes each utterance
by itself, has it transcribed by the Core's ``voice.transcribe`` and sends the transcript through the same
``respond`` route a typed message uses. The Core owns three things here:

* the owner's parameters, ``panel.json → voice.conversation`` (validated here, served to the page by
  ``GET /voice/status``; the page hard-codes none of them);
* the **reference rule** the page's detector follows, as a pure function tested on fixed level sequences --
  the page's JavaScript is a port of ``TurnDetector`` line for line (energy and duration only, no library,
  no recognition, nothing leaves the device but the closed utterance's WAV);
* ``is_noise``: a transcript with no words (``[BLANK_AUDIO]``, ``(música)``, punctuation) is never sent.

The rule, per audio frame with its RMS level ``level`` (0…1) and duration ``frame_ms``:

* the noise floor follows the level while nobody speaks (``floor = 0.95·floor + 0.05·level``) and the
  voiced threshold is ``max(min_level_permille/1000, 3·floor)`` (default ``MIN_LEVEL``);
* a voiced frame opens an utterance (``start``); inside it, voiced frames add speech, unvoiced ones add
  silence and a voiced frame clears the silence;
* ``silence_ms`` of silence closes it: ``end`` with at least ``min_speech_ms`` of speech, else ``drop``
  (a cough, a click -- dropped in the page, never sent);
* an utterance reaching ``max_utterance_s`` is closed as it is (``max``) -- never longer than the M22-33 cap.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Final, Mapping

__all__ = ["DEFAULTS", "MIN_LEVEL", "ConversationConfigError", "TurnDetector", "is_noise",
           "parse_conversation_section"]

MIN_LEVEL: Final[float] = 0.01
#: The owner's defaults (Q2, Q6): 900 ms of silence ends a turn; 300 ms of speech is the least that counts;
#: 30 s closes an utterance; 120 s without speech ends the session; 1.5 s to «Cancelar» before a send.
#: M25 (live M25-21, the owner: «hasta en silencio detecta cualquier ruido»): ``min_level_permille`` is the
#: least RMS level, in thousandths, that counts as voice -- 10 is ``MIN_LEVEL``; higher is less sensitive.
DEFAULTS: Final[Mapping[str, int]] = {"silence_ms": 900, "min_speech_ms": 300, "max_utterance_s": 30,
                                      "idle_s": 120, "grace_ms": 1500, "min_level_permille": 10}
_BOUNDS: Final[Mapping[str, tuple[int, int]]] = {
    "silence_ms": (300, 5000), "min_speech_ms": (100, 3000), "max_utterance_s": (5, 60),
    "idle_s": (15, 1800), "grace_ms": (0, 5000), "min_level_permille": (5, 300)}
#: What whisper writes for no words: bracketed or parenthesised tags, music notes, punctuation, space.
_TAGS: Final = re.compile(r"\[[^\]]*\]|\([^)]*\)|\*[^*]*\*|♪+")
_WORD: Final = re.compile(r"\w", re.UNICODE)


class ConversationConfigError(ValueError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def parse_conversation_section(raw: Any) -> dict[str, int] | None:
    """``voice.conversation``: ``true`` (the defaults) or a mapping of some of ``DEFAULTS``' keys, each an
    integer within its bounds; absent or ``false`` -- «Conversar» is not offered. A bad entry stops the
    panel with ``voice_conversation_invalid``."""
    if raw is None or raw is False:
        return None
    if raw is True:
        return dict(DEFAULTS)
    if not isinstance(raw, Mapping) or not set(raw) <= set(DEFAULTS):
        raise ConversationConfigError("voice_conversation_invalid")
    out = dict(DEFAULTS)
    for key, value in raw.items():
        low, high = _BOUNDS[key]
        if type(value) is not int or not low <= value <= high:
            raise ConversationConfigError("voice_conversation_invalid")
        out[key] = value
    return out   # the bounds keep min_speech_ms (≤ 3 s) below max_utterance_s (≥ 5 s)


def is_noise(text: Any) -> bool:
    """True when a transcript carries no word: only tags, notes, punctuation or space."""
    if not isinstance(text, str):
        return True
    return _WORD.search(_TAGS.sub(" ", text)) is None


@dataclass
class TurnDetector:
    """The reference end-of-turn rule (see the module docstring); ``feed`` returns ``start``, ``end``,
    ``drop``, ``max`` or ``None`` for each frame."""

    silence_ms: int = DEFAULTS["silence_ms"]
    min_speech_ms: int = DEFAULTS["min_speech_ms"]
    max_utterance_s: int = DEFAULTS["max_utterance_s"]
    min_level_permille: int = DEFAULTS["min_level_permille"]
    floor: float | None = None
    speaking: bool = False
    speech: float = 0.0
    silence: float = 0.0
    length: float = 0.0

    @classmethod
    def of(cls, params: Mapping[str, int]) -> "TurnDetector":
        return cls(silence_ms=params["silence_ms"], min_speech_ms=params["min_speech_ms"],
                   max_utterance_s=params["max_utterance_s"],
                   min_level_permille=params.get("min_level_permille", DEFAULTS["min_level_permille"]))

    def reset(self) -> None:
        self.speaking = False
        self.speech = self.silence = self.length = 0.0

    def feed(self, level: float, frame_ms: float) -> str | None:
        level = max(0.0, float(level))
        if self.floor is None:
            self.floor = level
        voiced = level >= max(self.min_level_permille / 1000, 3.0 * self.floor)
        if not self.speaking:
            if not voiced:
                self.floor = 0.95 * self.floor + 0.05 * level
                return None
            self.speaking = True
            self.speech, self.silence, self.length = frame_ms, 0.0, frame_ms
            return "start"
        self.length += frame_ms
        if voiced:
            self.speech += frame_ms
            self.silence = 0.0
        else:
            self.silence += frame_ms
        if self.length >= self.max_utterance_s * 1000:
            self.reset()
            return "max"
        if self.silence >= self.silence_ms:
            enough = self.speech >= self.min_speech_ms
            self.reset()
            return "end" if enough else "drop"
        return None
