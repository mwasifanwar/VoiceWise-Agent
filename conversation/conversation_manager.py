from .intent_recognition import recognize_intent
from .response_generator import generate_response

class ConversationManager:
    def __init__(self, config):
        self.config = config

    def handle_query(self, query):
        intent = recognize_intent(query)
        response = generate_response(intent, self.config)
        return response
