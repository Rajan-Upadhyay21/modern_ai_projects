def validate_feature_row(row):
    if row["purchase_count_30d"] < 0:
        return False, "purchase_count_30d cannot be negative"
    if row["avg_order_value"] < 0:
        return False, "avg_order_value cannot be negative"
    return True, "Valid feature row"

sample_row = {
    "purchase_count_30d": 4,
    "avg_order_value": 99.5
}

is_valid, message = validate_feature_row(sample_row)

print("Feature Validation Result:", is_valid)
print("Message:", message)
