context = {
    "What is AI?": "AI stands for artificial intelligence.",
    "What is NLP?": "NLP stands for natural language processing.",
    "What is RAG?": "RAG stands for retrieval-augmented generation."
}

question = "What is NLP?"
answer = context.get(question, "Answer not found.")

print("Question:", question)
print("Answer:", answer)
