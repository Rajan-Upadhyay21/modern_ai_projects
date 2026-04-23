relevant_items = {"doc_1", "doc_3", "doc_5"}
retrieved_items = ["doc_1", "doc_2", "doc_3", "doc_4"]

hits = len(set(retrieved_items) & relevant_items)
precision_at_k = hits / len(retrieved_items)
recall_at_k = hits / len(relevant_items)

print("Ranking Metrics:")
print("Precision@K:", precision_at_k)
print("Recall@K:", recall_at_k)
