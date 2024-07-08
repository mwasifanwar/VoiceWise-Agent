def recognize_intent(query):
    if "hello" in query:
        return "greeting"
    elif "name" in query:
        return "name_query"
    elif "how are you" in query:
        return "status_query"
    elif "bye" in query:
        return "farewell"
    else:
        return "unknown"
