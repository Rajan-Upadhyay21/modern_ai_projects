def coding_agent(task):
    steps = [
        "analyze code requirement",
        "select implementation approach",
        "generate code structure",
        "review output for improvement"
    ]

    return {
        "task": task,
        "steps": steps,
        "result": f"Code plan created for: {task}"
    }

result = coding_agent("Build a Python script for text classification")

print("Task:")
print(result["task"])

print("\nCoding Steps:")
for step in result["steps"]:
    print(step)

print("\nResult:")
print(result["result"])
