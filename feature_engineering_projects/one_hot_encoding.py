import pandas as pd

data = pd.DataFrame({
    "department": ["HR", "IT", "Finance", "IT"]
})

encoded = pd.get_dummies(data, columns=["department"])

print("One-Hot Encoded Data:")
print(encoded)
