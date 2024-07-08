import unittest
from config import Config
from conversation.conversation_manager import ConversationManager

class TestConversationManager(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.manager = ConversationManager(self.config)

    def test_handle_query_greeting(self):
        self.assertEqual(self.manager.handle_query("hello"), "Hi there! How can I assist you today?")

    def test_handle_query_unknown(self):
        self.assertEqual(self.manager.handle_query("unknown query"), "I'm sorry, I don't understand that.")

if __name__ == '__main__':
    unittest.main()
