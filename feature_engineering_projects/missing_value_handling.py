
Code files:

## `missing_value_handling.py`

```python
import pandas as pd

data = pd.DataFrame({
    "age": [25, None, 32, 28],
    "salary": [50000, 62000, None, 58000]
})

filled = data.fillna(data.mean(numeric_only=True))

print("Original Data:")
print(data)

print("\nAfter Missing Value Handling:")
print(filled)
