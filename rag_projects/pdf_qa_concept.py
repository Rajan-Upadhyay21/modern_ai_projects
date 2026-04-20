pdf_pages = [
    "Page 1: Introduction to AI systems.",
    "Page 2: RAG combines retrieval and generation.",
    "Page 3: Embeddings help semantic search."
]

question = "What does RAG combine?"

matching_pages = [page for page in pdf_pages if "RAG" in page]

print("Question:")
print(question)

print("\nRelevant Page Content:")
for page in matching_pages:
    print(page)
