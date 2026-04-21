def extract_data():
    return "Data extracted"

def validate_data():
    return "Data validated"

def train_model():
    return "Model trained"

def evaluate_model():
    return "Model evaluated"

def register_model():
    return "Model registered"

pipeline_steps = [
    extract_data(),
    validate_data(),
    train_model(),
    evaluate_model(),
    register_model()
]

print("Pipeline Orchestration Steps:")
for step_number, step in enumerate(pipeline_steps, start=1):
    print(f"Step {step_number}: {step}")
