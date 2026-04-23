import numpy as np

weights = np.array([0.9, 0.02, -0.01, 0.7, 0.003, -0.8, 0.05])
threshold = 0.05

pruned_weights = np.where(np.abs(weights) < threshold, 0, weights)

print("Original Weights:")
print(weights)

print("\nPruned Weights:")
print(pruned_weights)
