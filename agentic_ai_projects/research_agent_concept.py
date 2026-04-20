def research_agent(question):
    plan = [
        "identify research topic",
        "retrieve related information",
        "summarize findings",
        "prepare final response"
    ]

    return {
        "question": question,
        "plan": plan,
        "result": f"Research summary prepared for: {question}"
    }

result = research_agent("What are the main uses of RAG systems?")

print("Question:")
print(result["question"])

print("\nResearch Plan:")
for step in result["plan"]:
    print(step)

print("\nResult:")
print(result["result"])
