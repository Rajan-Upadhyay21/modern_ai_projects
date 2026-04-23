cache = {}

def predict(features):
    key = tuple(sorted(features.items()))
    if key in cache:
        return cache[key], "cache_hit"

    prediction = round((features["feature_1"] * 0.7) + (features["feature_2"] * 0.3), 2)
    cache[key] = prediction
    return prediction, "cache_miss"

request = {"feature_1": 0.9, "feature_2": 1.1}

first_prediction, first_status = predict(request)
second_prediction, second_status = predict(request)

print("Caching for Inference:")
print("First call:", first_prediction, first_status)
print("Second call:", second_prediction, second_status)
