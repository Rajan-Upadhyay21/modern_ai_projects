import pandas as pd

input_batch = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "feature_1": [0.8, 0.4, 0.9],
    "feature_2": [1.2, 0.7, 1.5]
})

def mock_predict(row):
    return round((row["feature_1"] + row["feature_2"]) / 2, 2)

input_batch["prediction"] = input_batch.apply(mock_predict, axis=1)

print("Batch Inference Results:")
print(input_batch)
