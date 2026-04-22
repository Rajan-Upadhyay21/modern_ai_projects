steps = [
    "Start from random Gaussian noise",
    "Apply denoising model at each timestep",
    "Refine the sample progressively",
    "Generate final image representation"
]

print("Image Generation Pipeline:")
for step_number, step in enumerate(steps, start=1):
    print(f"Step {step_number}: {step}")
