def serve_prediction(user_role, request_data):
    if user_role not in ["admin", "analyst", "approved_user"]:
        return {"status": "denied", "message": "Unauthorized access"}

    if "input" not in request_data:
        return {"status": "error", "message": "Missing input data"}

    return {
        "status": "success",
        "prediction": "approved_prediction_output"
    }

response = serve_prediction("approved_user", {"input": [1.2, 3.4, 5.6]})

print("Service Response:")
print(response)
