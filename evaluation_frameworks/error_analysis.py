errors = [
    {"sample_id": 1, "true": "positive", "predicted": "negative"},
    {"sample_id": 2, "true": "spam", "predicted": "not_spam"},
    {"sample_id": 3, "true": "class_A", "predicted": "class_B"}
]

print("Error Analysis:")
for error in errors:
    print(error)
