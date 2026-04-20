def support_agent(user_issue):
    if "refund" in user_issue.lower():
        workflow = ["identify refund policy", "retrieve refund steps", "generate support reply"]
    elif "password" in user_issue.lower():
        workflow = ["retrieve reset instructions", "generate help response"]
    else:
        workflow = ["analyze issue", "retrieve support guidance", "generate response"]

    return workflow

issue = "I need help with a refund request"
workflow = support_agent(issue)

print("User Issue:")
print(issue)

print("\nSupport Workflow:")
for step in workflow:
    print(step)
