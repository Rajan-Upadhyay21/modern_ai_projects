audit_records = [
    {"user": "ml_engineer", "action": "updated_threshold", "target": "error_rate_alert"},
    {"user": "ops_team", "action": "acknowledged_alert", "target": "latency_spike"},
    {"user": "reviewer", "action": "inspected_drift_report", "target": "feature_drift_score"}
]

print("Audit Trail:")
for record in audit_records:
    print(record)
