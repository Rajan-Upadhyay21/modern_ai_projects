import pandas as pd

data = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "purchase_amount": [120.5, 89.0, 210.3, 75.2]
})

data["amount_bucket"] = data["purchase_amount"].apply(
    lambda x: "high" if x >= 150 else "medium" if x >= 100 else "low"
)

print("Batch Processed Data:")
print(data)
