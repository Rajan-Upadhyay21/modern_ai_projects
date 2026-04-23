existing_ids = {101, 102, 103}
new_records = [
    {"customer_id": 103, "purchase_amount": 210.3},
    {"customer_id": 104, "purchase_amount": 75.2},
    {"customer_id": 105, "purchase_amount": 98.7}
]

incremental_updates = [record for record in new_records if record["customer_id"] not in existing_ids]

print("Incremental Updates:")
for record in incremental_updates:
    print(record)
