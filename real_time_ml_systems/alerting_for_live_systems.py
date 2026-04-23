metrics = {
    "latency_ms": 240,
    "error_rate": 0.06,
    "queue_depth": 120
}

thresholds = {
    "latency_ms": 200,
    "error_rate": 0.05,
    "queue_depth": 100
}

print("Alerting for Live Systems:")
for metric_name, value in metrics.items():
    threshold = thresholds[metric_name]
    is_alert = value > threshold
    print(f"{metric_name}: value={value}, threshold={threshold}, alert={is_alert}")
