record = {
    "customer_id": 101,
    "purchase_amount": 120.5,
    "country": "US"
}

expected_schema = {
    "customer_id": int,
    "purchase_amount": float,
    "country": str
}

valid = True

for field, field_type in expected_schema.items():
    if field not in record or not isinstance(record[field], field_type):
        valid = False
        print(f"Schema mismatch in field: {field}")

print("Schema Valid:", valid)
