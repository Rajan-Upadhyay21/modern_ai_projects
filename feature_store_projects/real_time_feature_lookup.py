online_feature_store = {
    101: {"purchase_count_30d": 5, "avg_order_value": 120.5},
    102: {"purchase_count_30d": 2, "avg_order_value": 89.0},
    103: {"purchase_count_30d": 8, "avg_order_value": 210.3}
}

customer_id = 102
features = online_feature_store.get(customer_id, {})

print("Real-Time Feature Lookup:")
print(f"Customer ID: {customer_id}")
print("Features:", features)
