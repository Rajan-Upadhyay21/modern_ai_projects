question = "How does RAG improve AI answers?"

context = """
RAG systems retrieve relevant documents before generation.
The retrieved content is inserted into the model prompt.
This improves grounding and response relevance.
""".strip()

prompt = f"""
You are a helpful AI assistant.

Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
""".strip()

print(prompt)
