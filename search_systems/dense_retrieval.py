import numpy as np
from sklearn.neighbors import NearestNeighbors

documents = ["doc_1", "doc_2", "doc_3", "doc_4"]
vectors = np.array([
    [0.90, 0.10, 0.20],
    [0.18, 0.92, 0.24],
    [0.20, 0.25, 0.95],
    [0.87, 0.11, 0.21]
])

query_vector = np.array([[0.89, 0.10, 0.22]])

nn = NearestNeighbors(n_neighbors=2, metric="cosine")
nn.fit(vectors)
distances, indices = nn.kneighbors(query_vector)

print("Dense Retrieval Results:")
for distance, idx in zip(distances[0], indices[0]):
    print(f"{documents[idx]} -> distance: {distance:.4f}")
