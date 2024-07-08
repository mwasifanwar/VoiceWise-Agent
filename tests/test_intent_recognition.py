import unittest
from conversation.intent_recognition import recognize_intent

class TestIntentRecognition(unittest.TestCase):
    def test_recognize_intent_greeting(self):
        self.assertEqual(recognize_intent("hello"), "greeting")

    def test_recognize_intent_unknown(self):
        self.assertEqual(recognize_intent("unknown query"), "unknown")

if __name__ == '__main__':
    unittest.main()
