feature_versions = {
    "customer_age": ["v1", "v2"],
    "purchase_frequency": ["v1", "v2", "v3"],
    "average_order_value": ["v1"]
}

print("Feature Versioning:")
for feature_name, versions in feature_versions.items():
    print(f"{feature_name}: {versions}")
