predictions = [
    {"confidence": 0.90, "correct": 1},
    {"confidence": 0.80, "correct": 1},
    {"confidence": 0.70, "correct": 0},
    {"confidence": 0.60, "correct": 1}
]

average_confidence = sum(item["confidence"] for item in predictions) / len(predictions)
average_accuracy = sum(item["correct"] for item in predictions) / len(predictions)

print("Calibration Concept:")
print("Average Confidence:", average_confidence)
print("Average Accuracy:", average_accuracy)
