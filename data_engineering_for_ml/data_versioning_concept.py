dataset_versions = {
    "v1": "raw_transactions_january",
    "v2": "cleaned_transactions_january",
    "v3": "feature_ready_transactions_january"
}

print("Data Versioning Concept:")
for version, description in dataset_versions.items():
    print(f"{version}: {description}")
