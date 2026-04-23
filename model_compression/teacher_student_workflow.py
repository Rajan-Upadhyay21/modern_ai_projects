workflow_steps = [
    "Train large teacher model",
    "Generate teacher outputs or soft labels",
    "Train smaller student model using teacher guidance",
    "Evaluate compressed student model"
]

print("Teacher-Student Workflow:")
for step_number, step in enumerate(workflow_steps, start=1):
    print(f"Step {step_number}: {step}")
