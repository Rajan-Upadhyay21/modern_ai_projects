import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "machine learning improves search systems",
    "deep learning supports computer vision",
    "retrieval augmented generation uses semantic search"
]

document_vectors = np.array([
    [0.92, 0.11, 0.20],
    [0.15, 0.94, 0.22],
    [0.20, 0.25, 0.97]
])

query = "semantic retrieval for search"
query_vector = np.array([[0.18, 0.20, 0.95]])

scores = cosine_similarity(query_vector, document_vectors)[0]

print("Semantic Search Results:")
for doc, score in sorted(zip(documents, scores), key=lambda x: x[1], reverse=True):
    print(f"{doc} -> {score:.4f}")
