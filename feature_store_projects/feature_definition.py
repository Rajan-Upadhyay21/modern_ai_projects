feature_definition = {
    "name": "customer_last_purchase_amount",
    "type": "numerical",
    "source": "transactions_table",
    "description": "Most recent purchase amount for each customer"
}

print("Feature Definition:")
for key, value in feature_definition.items():
    print(f"{key}: {value}")
