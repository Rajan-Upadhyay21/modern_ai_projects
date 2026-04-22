feature_registry = {
    "customer_last_purchase_amount": {
        "owner": "growth_team",
        "type": "numerical",
        "status": "active"
    },
    "customer_total_orders_30d": {
        "owner": "retention_team",
        "type": "numerical",
        "status": "active"
    }
}

print("Feature Registry:")
for feature_name, metadata in feature_registry.items():
    print(f"{feature_name} -> {metadata}")
