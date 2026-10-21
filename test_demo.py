import unittest
from dataclasses import FrozenInstanceError
from demo import Conversation


class ContinuityTests(unittest.TestCase):
    def test_swap_preserves_history_and_context(self):
        conversation = Conversation()
        conversation.turn("fake-a", "Synthetic task")
        before = conversation.history
        response = conversation.turn("fake-b", "Continue")
        self.assertEqual(conversation.history[:2], before)
        self.assertIn("prior user messages=1", response)
        self.assertEqual([event.seq for event in conversation.history], [1, 2, 3, 4])

    def test_unknown_adapter_does_not_mutate_history(self):
        conversation = Conversation()
        conversation.turn("fake-a", "Synthetic task")
        before = conversation.history
        with self.assertRaises(ValueError):
            conversation.turn("unknown", "Continue")
        self.assertEqual(conversation.history, before)

    def test_snapshot_is_immutable_and_remains_stable(self):
        conversation = Conversation()
        conversation.turn("fake-a", "Synthetic task")
        snapshot = conversation.history
        with self.assertRaises(FrozenInstanceError):
            snapshot[0].content = "Changed"
        conversation.turn("fake-b", "Continue")
        self.assertEqual(len(snapshot), 2)
        self.assertEqual(snapshot[0].content, "Synthetic task")


if __name__ == "__main__":
    unittest.main()
