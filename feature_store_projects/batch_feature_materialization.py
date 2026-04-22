import pandas as pd

features = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "purchase_count_30d": [5, 2, 8],
    "avg_order_value": [120.5, 89.0, 210.3]
})

print("Batch Feature Materialization Output:")
print(features)
