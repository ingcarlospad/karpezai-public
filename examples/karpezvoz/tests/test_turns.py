"""Public tests of actual extracted source, using only synthetic level sequences."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from demo import scenario, SCENARIOS
from turns import TurnDetector, parse_conversation_section, ConversationConfigError, is_noise


class VoiceTurnTests(unittest.TestCase):
    def test_short_sound_is_discarded(self):
        self.assertEqual(scenario(SCENARIOS['Ruido corto: descartar']), ['start', 'drop'])

    def test_valid_speech_ends_after_silence(self):
        self.assertEqual(scenario(SCENARIOS['Voz suficiente: cerrar turno']), ['start', 'end'])

    def test_silence_never_starts_turn(self):
        self.assertEqual(scenario(SCENARIOS['Silencio: no enviar']), [])

    def test_hard_duration_limit_closes_turn(self):
        self.assertEqual(scenario(SCENARIOS['Limite temporal: cerrar']), ['start', 'max'])

    def test_speech_resuming_before_timeout_clears_silence(self):
        detector = TurnDetector()
        detector.feed(0.001, 100)
        self.assertEqual(detector.feed(0.1, 300), 'start')
        self.assertIsNone(detector.feed(0.001, 800))
        self.assertIsNone(detector.feed(0.1, 100))
        self.assertIsNone(detector.feed(0.001, 800))
        self.assertEqual(detector.feed(0.001, 100), 'end')

    def test_end_resets_detector_for_next_turn(self):
        detector = TurnDetector()
        detector.feed(0.001, 100)
        detector.feed(0.1, 300)
        self.assertEqual(detector.feed(0.001, 900), 'end')
        self.assertFalse(detector.speaking)
        self.assertEqual(detector.feed(0.1, 300), 'start')

    def test_invalid_configuration_is_rejected(self):
        for invalid in ({'silence_ms': 1}, {'silence_ms': True}, {'unknown': 1}, 'enabled'):
            with self.subTest(invalid=invalid), self.assertRaises(ConversationConfigError):
                parse_conversation_section(invalid)

    def test_noise_tags_are_not_words_but_normal_speech_is(self):
        self.assertTrue(is_noise('[musica] ...'))
        self.assertFalse(is_noise('Hola, esto es una prueba'))


if __name__ == '__main__':
    unittest.main()
