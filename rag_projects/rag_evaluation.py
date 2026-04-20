retrieved_docs = [
    "RAG combines retrieval and generation.",
    "Transformers are useful for NLP.",
    "Embeddings help semantic similarity."
]

relevant_docs = {
    "RAG combines retrieval and generation.",
    "Embeddings help semantic similarity."
}

hits = len(set(retrieved_docs) & relevant_docs)

precision_at_k = hits / len(retrieved_docs)
recall_at_k = hits / len(relevant_docs)

print("Precision@K:", precision_at_k)
print("Recall@K:", recall_at_k)
