trace = {
    "request_id": "req_1001",
    "user_id": "user_42",
    "steps": [
        "request_received",
        "input_validated",
        "features_loaded",
        "model_invoked",
        "response_returned"
    ]
}

print("Request Trace:")
for key, value in trace.items():
    print(f"{key}: {value}")
