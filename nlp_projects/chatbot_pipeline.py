def chatbot_response(user_message):
    message = user_message.lower()

    if "hello" in message:
        return "Hello! How can I help you today?"
    if "ai" in message:
        return "AI stands for artificial intelligence."
    if "bye" in message:
        return "Goodbye! Have a great day."
    return "I am not sure, but I can try to help."

messages = ["Hello", "What is AI?", "Bye"]

for msg in messages:
    print("User:", msg)
    print("Bot:", chatbot_response(msg))
    print("-" * 30)
