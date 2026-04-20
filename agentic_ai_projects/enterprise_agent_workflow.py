def receive_request(user_request):
    return f"Received enterprise request: {user_request}"

def classify_request(user_request):
    if "policy" in user_request.lower():
        return "policy_lookup"
    if "report" in user_request.lower():
        return "report_analysis"
    return "general_assistance"

def execute_workflow(workflow_type):
    if workflow_type == "policy_lookup":
        return ["retrieve policy documents", "extract relevant policy text", "prepare answer"]
    if workflow_type == "report_analysis":
        return ["load report", "summarize findings", "prepare insights"]
    return ["analyze request", "prepare general response"]

request = "Find the latest travel policy for employees"

print(receive_request(request))

workflow_type = classify_request(request)
steps = execute_workflow(workflow_type)

print("\nWorkflow Type:")
print(workflow_type)

print("\nWorkflow Steps:")
for step in steps:
    print(step)
