online_store = {
    101: {"purchase_count_30d": 5, "avg_order_value": 120.5},
    102: {"purchase_count_30d": 2, "avg_order_value": 89.0},
    103: {"purchase_count_30d": 8, "avg_order_value": 210.3}
}

customer_id = 101
features = online_store.get(customer_id, {})

print("Online Feature Lookup:")
print("Customer ID:", customer_id)
print("Features:", features)
