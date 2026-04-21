def validate_request(data):
    required_fields = ["age", "income"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"

    if not isinstance(data["age"], (int, float)):
        return False, "Age must be numeric"

    if not isinstance(data["income"], (int, float)):
        return False, "Income must be numeric"

    if data["age"] < 0:
        return False, "Age cannot be negative"

    if data["income"] < 0:
        return False, "Income cannot be negative"

    return True, "Request valid"

sample_request = {"age": 29, "income": 60000}

is_valid, message = validate_request(sample_request)

print("Validation Result:", is_valid)
print("Message:", message)
