def on_event(event):
    if event["type"] == "purchase":
        return "Trigger fraud score update"
    if event["type"] == "click":
        return "Trigger recommendation refresh"
    return "No action"

events = [
    {"event_id": 1, "type": "purchase"},
    {"event_id": 2, "type": "click"},
    {"event_id": 3, "type": "login"}
]

print("Event-Driven Pipeline:")
for event in events:
    action = on_event(event)
    print(f"Event {event['event_id']} -> {action}")
