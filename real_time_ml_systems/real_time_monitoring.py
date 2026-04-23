import numpy as np

latencies = np.array([18, 21, 17, 23, 19, 20])
scores = np.array([0.82, 0.85, 0.80, 0.88, 0.84, 0.83])

print("Real-Time Monitoring:")
print("Average Latency (ms):", latencies.mean())
print("Max Latency (ms):", latencies.max())
print("Average Prediction Score:", scores.mean())
