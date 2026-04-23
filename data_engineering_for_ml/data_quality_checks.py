import pandas as pd

data = pd.DataFrame({
    "customer_id": [101, 102, None, 104],
    "purchase_amount": [120.5, -10.0, 210.3, 75.2]
})

missing_customer_ids = data["customer_id"].isnull().sum()
negative_amounts = (data["purchase_amount"] < 0).sum()

print("Data Quality Checks:")
print("Missing customer_id values:", missing_customer_ids)
print("Negative purchase_amount values:", negative_amounts)
