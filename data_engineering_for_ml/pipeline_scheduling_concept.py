scheduled_jobs = [
    {"job": "daily_ingestion", "schedule": "every day at 1 AM"},
    {"job": "feature_refresh", "schedule": "every day at 2 AM"},
    {"job": "training_dataset_build", "schedule": "every Sunday at 3 AM"}
]

print("Pipeline Scheduling Concept:")
for job in scheduled_jobs:
    print(job)
