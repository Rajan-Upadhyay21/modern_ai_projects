workflow_steps = [
    "read raw batch data",
    "clean and transform records",
    "store processed output in parquet format",
    "load parquet for model training"
]

print("Parquet Workflow:")
for step_number, step in enumerate(workflow_steps, start=1):
    print(f"Step {step_number}: {step}")
