import pandas as pd

data = pd.DataFrame({
    "city": ["Chicago", "New York", "Chicago", "Boston"]
})

encoded = data.copy()
encoded["city_code"] = encoded["city"].astype("category").cat.codes

print("Original Data:")
print(data)

print("\nCategorical Encoding:")
print(encoded)
