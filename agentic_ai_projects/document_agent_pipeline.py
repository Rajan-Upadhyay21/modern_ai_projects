def document_agent(document_question):
    retrieved_sections = [
        "Section 1: Company leave policy overview",
        "Section 2: Paid leave eligibility details"
    ]

    answer = f"Answer based on retrieved document sections for question: {document_question}"

    return retrieved_sections, answer

question = "What is the leave eligibility policy?"
sections, answer = document_agent(question)

print("Question:")
print(question)

print("\nRetrieved Sections:")
for section in sections:
    print(section)

print("\nAnswer:")
print(answer)
