retrieved_results = ["doc_1", "doc_2", "doc_3", "doc_4"]
relevant_results = {"doc_1", "doc_3", "doc_5"}

hits = len(set(retrieved_results) & relevant_results)
precision_at_k = hits / len(retrieved_results)
recall_at_k = hits / len(relevant_results)

print("Retrieved Results:")
print(retrieved_results)

print("\nRelevant Results:")
print(relevant_results)

print("\nPrecision@K:", precision_at_k)
print("Recall@K:", recall_at_k)
