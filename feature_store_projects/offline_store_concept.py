offline_store = {
    "storage_type": "historical batch storage",
    "main_use": "training and backfilling",
    "examples": ["data warehouse", "data lake", "parquet files"]
}

print("Offline Store Concept:")
for key, value in offline_store.items():
    print(f"{key}: {value}")
