def define_feature():
    return "Define feature and metadata"

def compute_feature():
    return "Compute feature from source data"

def validate_feature():
    return "Validate feature quality"

def store_offline():
    return "Store feature in offline store"

def serve_online():
    return "Serve feature in online store"

workflow_steps = [
    define_feature(),
    compute_feature(),
    validate_feature(),
    store_offline(),
    serve_online()
]

print("End-to-End Feature Store Workflow:")
for step_number, step in enumerate(workflow_steps, start=1):
    print(f"Step {step_number}: {step}")
