def ingest_data():
    return "Ingest raw data"

def clean_data():
    return "Clean and standardize records"

def validate_schema():
    return "Validate schema and required fields"

def prepare_features():
    return "Prepare model features"

def construct_dataset():
    return "Construct final ML-ready dataset"

workflow_steps = [
    ingest_data(),
    clean_data(),
    validate_schema(),
    prepare_features(),
    construct_dataset()
]

print("End-to-End Data Pipeline:")
for step_number, step in enumerate(workflow_steps, start=1):
    print(f"Step {step_number}: {step}")
