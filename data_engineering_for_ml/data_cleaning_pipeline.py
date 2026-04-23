import pandas as pd

data = pd.DataFrame({
    "customer_id": [101, 102, 103, None],
    "purchase_amount": [120.5, None, 210.3, 75.2],
    "country": ["US", "US", None, "CA"]
})

cleaned = data.dropna()

print("Original Data:")
print(data)

print("\nCleaned Data:")
print(cleaned)
