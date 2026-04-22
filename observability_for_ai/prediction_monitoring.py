import numpy as np

predictions = np.array([0.82, 0.88, 0.91, 0.79, 0.84, 0.87])

print("Prediction Monitoring:")
print("Mean Prediction Score:", predictions.mean())
print("Min Prediction Score:", predictions.min())
print("Max Prediction Score:", predictions.max())
print("Prediction Std:", predictions.std())
