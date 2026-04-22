import numpy as np

latencies_ms = np.array([120, 130, 128, 140, 150, 135, 125])

print("Latency Monitoring:")
print("Average Latency:", latencies_ms.mean())
print("P95 Approximation:", np.percentile(latencies_ms, 95))
print("Max Latency:", latencies_ms.max())
