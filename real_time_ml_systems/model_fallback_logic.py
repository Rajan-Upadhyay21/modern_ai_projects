def primary_model(features):
    raise RuntimeError("Primary model unavailable")

def fallback_model(features):
    return round((features["feature_1"] + features["feature_2"]) / 2, 2)

features = {"feature_1": 0.8, "feature_2": 1.2}

try:
    prediction = primary_model(features)
    source = "primary_model"
except Exception:
    prediction = fallback_model(features)
    source = "fallback_model"

print("Model Fallback Logic:")
print("Prediction:", prediction)
print("Served By:", source)
