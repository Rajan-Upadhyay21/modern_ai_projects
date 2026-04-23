
Code files:

## `data_ingestion.py`

```python
import pandas as pd

raw_data = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "purchase_amount": [120.5, 89.0, 210.3],
    "country": ["US", "US", "CA"]
})

print("Ingested Raw Data:")
print(raw_data)
