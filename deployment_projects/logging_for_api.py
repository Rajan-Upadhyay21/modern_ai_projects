logs = []

def log_request(endpoint, method, status_code):
    logs.append({
        "endpoint": endpoint,
        "method": method,
        "status_code": status_code
    })

log_request("/predict", "POST", 200)
log_request("/health", "GET", 200)
log_request("/predict", "POST", 400)

print("API Logs:")
for log in logs:
    print(log)
