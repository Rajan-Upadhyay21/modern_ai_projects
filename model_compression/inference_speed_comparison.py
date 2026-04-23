models = [
    {"name": "teacher_model", "latency_ms": 120},
    {"name": "compressed_model", "latency_ms": 45}
]

print("Inference Speed Comparison:")
for model in models:
    print(model)
