alerts = []

def create_alert(alert_type, severity, message):
    alerts.append({
        "type": alert_type,
        "severity": severity,
        "message": message
    })

create_alert("drift_detection", "high", "Input distribution drift exceeded threshold.")
create_alert("model_monitoring", "medium", "Prediction confidence dropped below expected range.")

print("Generated Alerts:")
for alert in alerts:
    print(alert)
