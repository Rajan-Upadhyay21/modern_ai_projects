def validate_request(request):
    return "input" in request

def detect_prompt_risk(prompt):
    blocked_patterns = ["ignore previous instructions", "bypass safety"]
    return any(pattern in prompt.lower() for pattern in blocked_patterns)

def run_model(request):
    return {"prediction": "safe_output"}

def filter_output(output):
    return output

request = {
    "input": "Summarize this document",
    "prompt": "Please summarize the uploaded file."
}

print("Step 1: Validate request")
if not validate_request(request):
    print("Request rejected: invalid input")
else:
    print("Request valid")

    print("\nStep 2: Detect prompt risk")
    if detect_prompt_risk(request["prompt"]):
        print("Request rejected: risky prompt detected")
    else:
        print("Prompt accepted")

        print("\nStep 3: Run model")
        output = run_model(request)
        print(output)

        print("\nStep 4: Filter output")
        safe_output = filter_output(output)
        print(safe_output)
