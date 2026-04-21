import numpy as np

prediction_scores = np.array([0.82, 0.84, 0.80, 0.79, 0.88, 0.83])

print("Model Monitoring Statistics:")
print("Mean Prediction Score:", prediction_scores.mean())
print("Minimum Prediction Score:", prediction_scores.min())
print("Maximum Prediction Score:", prediction_scores.max())
print("Standard Deviation:", prediction_scores.std())
