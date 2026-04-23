
Code files:

## `streaming_inference.py`

```python
events = [
    {"event_id": 1, "feature_1": 0.8, "feature_2": 1.2},
    {"event_id": 2, "feature_1": 0.4, "feature_2": 0.7},
    {"event_id": 3, "feature_1": 0.9, "feature_2": 1.5}
]

def predict(event):
    return round((event["feature_1"] + event["feature_2"]) / 2, 2)

print("Streaming Inference:")
for event in events:
    prediction = predict(event)
    print(f"Event {event['event_id']} -> prediction: {prediction}")
