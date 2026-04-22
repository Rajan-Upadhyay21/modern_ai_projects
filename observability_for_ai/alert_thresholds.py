metrics = {
    "latency_ms": 220,
    "error_rate": 0.08,
    "drift_score": 6.1
}

thresholds = {
    "latency_ms": 200,
    "error_rate": 0.05,
    "drift_score": 5.0
}

print("Alert Checks:")
for metric_name, value in metrics.items():
    threshold = thresholds[metric_name]
    triggered = value > threshold
    print(f"{metric_name}: value={value}, threshold={threshold}, alert={triggered}")
