training_record = {
    "event_time": "2025-04-01 10:00:00",
    "feature_time_limit": "Only use feature values available before event_time"
}

print("Point-in-Time Correctness Concept:")
for key, value in training_record.items():
    print(f"{key}: {value}")

print("\nReason:")
print("This prevents data leakage from future information.")
