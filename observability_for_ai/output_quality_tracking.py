quality_records = [
    {"sample_id": 1, "expected": "positive", "predicted": "positive"},
    {"sample_id": 2, "expected": "negative", "predicted": "negative"},
    {"sample_id": 3, "expected": "positive", "predicted": "negative"},
    {"sample_id": 4, "expected": "positive", "predicted": "positive"}
]

correct = sum(item["expected"] == item["predicted"] for item in quality_records)
accuracy = correct / len(quality_records)

print("Output Quality Tracking:")
print("Accuracy:", accuracy)
print("Records:")
for item in quality_records:
    print(item)
