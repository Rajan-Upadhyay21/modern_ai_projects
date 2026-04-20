import numpy as np

request_sizes = np.array([120, 130, 128, 125, 500, 127, 129, 126])

mean = request_sizes.mean()
std = request_sizes.std()

z_scores = (request_sizes - mean) / std
anomalies = request_sizes[np.abs(z_scores) > 2]

print("Request Sizes:")
print(request_sizes)

print("\nZ-Scores:")
print(z_scores)

print("\nAnomalous Requests:")
print(anomalies)
