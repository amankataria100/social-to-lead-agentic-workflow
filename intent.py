def detect_intent(user_input: str):
    text = user_input.lower()

    greeting_words = ["hi", "hello", "hey"]
    product_words = ["price", "cost", "plan", "features"]
    high_intent_words = ["buy", "subscribe", "sign up", "interested", "try", "start", "demo"]

    if any(word in text for word in greeting_words):
        return "greeting"

    elif any(word in text for word in high_intent_words):
        return "high_intent"

    elif any(word in text for word in product_words):
        return "product_query"

    return "unknown"