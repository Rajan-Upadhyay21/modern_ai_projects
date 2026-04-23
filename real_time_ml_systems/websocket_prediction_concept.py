messages = [
    {"user_id": "u1", "text": "new event received"},
    {"user_id": "u2", "text": "score this action"},
    {"user_id": "u3", "text": "update recommendation"}
]

print("WebSocket Prediction Concept:")
for message in messages:
    print(f"Live message from {message['user_id']} -> {message['text']}")
