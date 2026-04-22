import numpy as np

true_noise = np.array([0.10, -0.04, 0.07, 0.02])
predicted_noise = np.array([0.08, -0.03, 0.06, 0.01])

mse_loss = np.mean((true_noise - predicted_noise) ** 2)

print("True Noise:")
print(true_noise)

print("\nPredicted Noise:")
print(predicted_noise)

print("\nTraining Objective (MSE Loss):")
print(mse_loss)
