import numpy as np

noisy_sample = np.array([0.52, 0.11, -0.08, 0.34])
predicted_noise = np.array([0.10, 0.03, -0.02, 0.08])

denoised_sample = noisy_sample - predicted_noise

print("Noisy Sample:")
print(noisy_sample)

print("\nPredicted Noise:")
print(predicted_noise)

print("\nDenoised Sample:")
print(denoised_sample)
