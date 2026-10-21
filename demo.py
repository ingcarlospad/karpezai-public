"""Synthetic educational example. Not the private KarpezAI runtime."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    seq: int
    role: str
    content: str


class Conversation:
    def __init__(self):
        self._events = []

    @property
    def history(self):
        return tuple(self._events)

    def turn(self, adapter, message):
        if adapter not in ("fake-a", "fake-b"):
            raise ValueError("Unknown adapter")
        prior_messages = sum(e.role == "user" for e in self._events)
        self._events.append(Event(len(self._events) + 1, "user", message))
        reply = f"{adapter}: prior user messages={prior_messages}; received={message}"
        self._events.append(Event(len(self._events) + 1, "assistant", reply))
        return reply


if __name__ == "__main__":
    conversation = Conversation()
    print(conversation.turn("fake-a", "Synthetic task"))
    print(conversation.turn("fake-b", "Continue synthetic task"))
    print(f"Preserved events: {len(conversation.history)}")
