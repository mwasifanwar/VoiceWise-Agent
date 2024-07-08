import unittest
from config import Config
from conversation.response_generator import generate_response

class TestResponseGenerator(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_generate_response_greeting(self):
        self.assertEqual(generate_response("greeting", self.config), "Hi there! How can I assist you today?")

    def test_generate_response_unknown(self):
        self.assertEqual(generate_response("unknown", self.config), "I'm sorry, I don't understand that.")

if __name__ == '__main__':
    unittest.main()
