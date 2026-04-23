events = [
    {"event_id": 1, "type": "purchase", "amount": 120.5},
    {"event_id": 2, "type": "click", "amount": 0},
    {"event_id": 3, "type": "purchase", "amount": 89.0}
]

print("Streaming Concept:")
for event in events:
    print("Processing event:", event)
