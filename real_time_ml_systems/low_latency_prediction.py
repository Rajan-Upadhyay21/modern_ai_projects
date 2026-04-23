import time

def predict(features):
    return round((features["feature_1"] * 0.6) + (features["feature_2"] * 0.4), 3)

request = {"feature_1": 0.82, "feature_2": 1.14}

start = time.time()
prediction = predict(request)
end = time.time()

latency_ms = (end - start) * 1000

print("Low-Latency Prediction:")
print("Prediction:", prediction)
print("Latency (ms):", latency_ms)
