import pandas as pd
import numpy as np

data = pd.DataFrame({
    "value": [10, 12, 11, 13, 100]
})

q1 = data["value"].quantile(0.25)
q3 = data["value"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

filtered = data[(data["value"] >= lower) & (data["value"] <= upper)]

print("Original Data:")
print(data)

print("\nAfter Outlier Handling:")
print(filtered)
