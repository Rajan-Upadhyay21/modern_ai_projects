import pandas as pd

data = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "purchase_amount": [120.5, 89.0, 210.3],
    "purchase_count": [5, 2, 8]
})

data["avg_purchase_proxy"] = data["purchase_amount"] / data["purchase_count"]

print("Prepared Features:")
print(data)
