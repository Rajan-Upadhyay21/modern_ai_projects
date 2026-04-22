training_feature_logic = "customer_total_orders_last_30_days"
serving_feature_logic = "customer_total_orders_last_30_days"

is_consistent = training_feature_logic == serving_feature_logic

print("Training Feature Logic:", training_feature_logic)
print("Serving Feature Logic:", serving_feature_logic)
print("Consistent:", is_consistent)
