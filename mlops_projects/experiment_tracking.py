
Code files:

## `experiment_tracking.py`

```python
experiments = [
    {"run_id": 1, "model": "RandomForest", "learning_rate": 0.01, "accuracy": 0.87},
    {"run_id": 2, "model": "XGBoost", "learning_rate": 0.005, "accuracy": 0.90},
    {"run_id": 3, "model": "NeuralNet", "learning_rate": 0.001, "accuracy": 0.92}
]

print("Experiment Tracking Records:")
for experiment in experiments:
    print(experiment)

best_run = max(experiments, key=lambda x: x["accuracy"])

print("\nBest Run:")
print(best_run)
