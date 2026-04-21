def validate_data():
    return "Data validation completed"

def track_experiment():
    return "Experiment tracked"

def register_model():
    return "Model registered"

def deploy_model():
    return "Model deployed to staging"

def monitor_model():
    return "Model monitoring started"

workflow_steps = [
    validate_data(),
    track_experiment(),
    register_model(),
    deploy_model(),
    monitor_model()
]

print("End-to-End MLOps Workflow:")
for step_number, step in enumerate(workflow_steps, start=1):
    print(f"Step {step_number}: {step}")
