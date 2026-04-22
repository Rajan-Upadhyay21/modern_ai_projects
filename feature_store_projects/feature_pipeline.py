def extract_raw_data():
    return "Extract raw source data"

def transform_features():
    return "Transform source data into model features"

def validate_features():
    return "Validate feature values and schema"

def publish_features():
    return "Publish features to store"

pipeline_steps = [
    extract_raw_data(),
    transform_features(),
    validate_features(),
    publish_features()
]

print("Feature Pipeline Steps:")
for step_number, step in enumerate(pipeline_steps, start=1):
    print(f"Step {step_number}: {step}")
