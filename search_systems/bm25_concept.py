documents = [
    {"doc": "machine learning improves search systems", "term_frequency": 2, "doc_length": 5},
    {"doc": "search systems use indexing and ranking", "term_frequency": 3, "doc_length": 6},
    {"doc": "ranking models improve retrieval quality", "term_frequency": 1, "doc_length": 5}
]

print("BM25 Concept:")
print("BM25 uses term frequency, document length, and inverse document frequency.")
print()

for item in documents:
    print(item)
