logs = []

def log_event(user, action, status):
    logs.append({
        "user": user,
        "action": action,
        "status": status
    })

log_event("analyst_user", "request_prediction", "success")
log_event("guest_user", "access_model_logs", "denied")
log_event("admin_user", "update_config", "success")

print("Audit Logs:")
for log in logs:
    print(log)
