models = [
    {"name": "RandomForest", "accuracy": 0.89, "latency_ms": 35},
    {"name": "XGBoost", "accuracy": 0.91, "latency_ms": 40},
    {"name": "NeuralNet", "accuracy": 0.93, "latency_ms": 55}
]

print("Model Comparison:")
for model in models:
    print(model)

best_model = max(models, key=lambda x: x["accuracy"])
print("\nBest Accuracy Model:")
print(best_model)
