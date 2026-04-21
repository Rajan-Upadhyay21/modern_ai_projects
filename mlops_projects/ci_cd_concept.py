ci_cd_steps = [
    "Run unit tests",
    "Validate data schema",
    "Train candidate model",
    "Evaluate performance thresholds",
    "Package model artifact",
    "Deploy to staging",
    "Promote to production if approved"
]

print("CI/CD Concept for ML:")
for step_number, step in enumerate(ci_cd_steps, start=1):
    print(f"Step {step_number}: {step}")
