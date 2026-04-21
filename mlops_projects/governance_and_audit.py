audit_log = [
    {"user": "ml_engineer", "action": "registered_model", "model_version": "v3"},
    {"user": "reviewer", "action": "approved_model", "model_version": "v3"},
    {"user": "ops_team", "action": "deployed_to_staging", "model_version": "v3"}
]

print("Governance and Audit Log:")
for entry in audit_log:
    print(entry)
