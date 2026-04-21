messages = {
    "A": ["message_from_B", "message_from_C"],
    "B": ["message_from_A"],
    "C": ["message_from_A"]
}

print("Message Passing Concept:")
for node, incoming_messages in messages.items():
    print(f"{node} receives: {incoming_messages}")
