import pandas as pd

data = pd.DataFrame({
    "date": ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02"],
    "customer_id": [101, 102, 103, 104],
    "purchase_amount": [120.5, 89.0, 210.3, 75.2]
})

partitions = {date: group for date, group in data.groupby("date")}

print("Data Partitions:")
for date, partition in partitions.items():
    print(f"\nPartition: {date}")
    print(partition)
