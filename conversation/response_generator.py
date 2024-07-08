def generate_response(intent, config):
    responses = {
        "greeting": config.greeting_message,
        "name_query": "I am an AI voice agent created to help you.",
        "status_query": "I am just a program, but thanks for asking!",
        "farewell": "Goodbye! Have a great day!",
        "unknown": config.fallback_message
    }
    
    return responses.get(intent, config.fallback_message)
