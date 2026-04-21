graph_embeddings = {
    "graph_1": [0.81, 0.22, 0.45],
    "graph_2": [0.15, 0.91, 0.38],
    "graph_3": [0.74, 0.19, 0.52]
}

print("Graph Embeddings:")
for graph_id, embedding in graph_embeddings.items():
    print(f"{graph_id} -> {embedding}")
