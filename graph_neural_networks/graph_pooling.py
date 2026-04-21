node_embeddings = {
    "A": [0.8, 0.2],
    "B": [0.6, 0.4],
    "C": [0.7, 0.3]
}

pooled_embedding = [
    sum(embedding[0] for embedding in node_embeddings.values()) / len(node_embeddings),
    sum(embedding[1] for embedding in node_embeddings.values()) / len(node_embeddings)
]

print("Node Embeddings:")
for node, embedding in node_embeddings.items():
    print(f"{node} -> {embedding}")

print("\nGraph Pooled Embedding:")
print(pooled_embedding)
