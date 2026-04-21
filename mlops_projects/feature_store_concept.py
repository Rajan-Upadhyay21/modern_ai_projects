feature_store = {
    "customer_age": {"source": "customer_profile_table", "type": "numerical"},
    "last_purchase_amount": {"source": "transactions_table", "type": "numerical"},
    "preferred_category": {"source": "user_behavior_table", "type": "categorical"}
}

print("Feature Store Concept:")
for feature_name, metadata in feature_store.items():
    print(f"{feature_name} -> {metadata}")
