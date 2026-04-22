import numpy as np

image = np.array([0.9, 0.8, 0.7, 0.6])
noise = np.random.normal(0, 0.1, size=image.shape)

noisy_image = image + noise

print("Original Image Representation:")
print(image)

print("\nSampled Noise:")
print(noise)

print("\nNoisy Image Representation:")
print(noisy_image)
