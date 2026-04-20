retrieved_chunks = [
    "RAG systems first retrieve relevant documents.",
    "The retrieved content is added to the generation prompt.",
    "This helps the final response stay grounded."
]

context = "\n".join(retrieved_chunks)

print("Built Context:")
print(context)
