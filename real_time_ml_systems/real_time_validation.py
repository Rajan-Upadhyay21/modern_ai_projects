def validate_request(data):
    required_fields = ["feature_1", "feature_2"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"

    if not isinstance(data["feature_1"], (int, float)):
        return False, "feature_1 must be numeric"

    if not isinstance(data["feature_2"], (int, float)):
        return False, "feature_2 must be numeric"

    return True, "Valid request"

incoming_request = {"feature_1": 0.75, "feature_2": 1.12}

is_valid, message = validate_request(incoming_request)

print("Real-Time Validation:")
print("Valid:", is_valid)
print("Message:", message)
