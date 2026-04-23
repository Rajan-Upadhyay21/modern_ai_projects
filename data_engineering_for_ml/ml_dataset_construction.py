import pandas as pd

raw_data = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "purchase_count": [5, 2, 8],
    "avg_order_value": [120.5, 89.0, 210.3],
    "churn_label": [0, 1, 0]
})

X = raw_data[["purchase_count", "avg_order_value"]]
y = raw_data["churn_label"]

print("ML Features:")
print(X)

print("\nTarget:")
print(y)
