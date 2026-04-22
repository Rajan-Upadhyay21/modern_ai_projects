def log_request():
    return "Log incoming request"

def trace_workflow():
    return "Trace request through system"

def monitor_predictions():
    return "Monitor model outputs"

def track_latency_and_errors():
    return "Track latency and error rate"

def detect_drift():
    return "Check feature and output drift"

def trigger_alerts():
    return "Trigger alerts if thresholds are crossed"

workflow_steps = [
    log_request(),
    trace_workflow(),
    monitor_predictions(),
    track_latency_and_errors(),
    detect_drift(),
    trigger_alerts()
]

print("End-to-End Observability Workflow:")
for step_number, step in enumerate(workflow_steps, start=1):
    print(f"Step {step_number}: {step}")
