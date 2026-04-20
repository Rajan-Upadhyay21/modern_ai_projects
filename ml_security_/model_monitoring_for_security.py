import numpy as np

prediction_confidences = np.array([0.92, 0.88, 0.91, 0.15, 0.89, 0.12])

print("Prediction Confidence Statistics:")
print("Mean:", prediction_confidences.mean())
print("Min:", prediction_confidences.min())
print("Max:", prediction_confidences.max())

low_confidence_count = np.sum(prediction_confidences < 0.2)
print("\nLow Confidence Outputs:", int(low_confidence_count))
