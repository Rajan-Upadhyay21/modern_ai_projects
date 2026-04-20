def validate_input(data):
    required_fields = ["age", "salary"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    if not isinstance(data["age"], (int, float)):
        return False, "Age must be numeric"

    if not isinstance(data["salary"], (int, float)):
        return False, "Salary must be numeric"

    if data["age"] < 0:
        return False, "Age cannot be negative"

    if data["salary"] < 0:
        return False, "Salary cannot be negative"

    return True, "Input is valid"

sample_input = {"age": 30, "salary": 65000}

is_valid, message = validate_input(sample_input)

print("Validation Result:", is_valid)
print("Message:", message)
