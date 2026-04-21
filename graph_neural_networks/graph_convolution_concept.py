node_features = {
    "A": [1.0, 0.0],
    "B": [0.5, 1.0],
    "C": [0.2, 0.8]
}

neighbors = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}

updated_features = {}

for node, nbrs in neighbors.items():
    aggregated = [0.0, 0.0]
    for nbr in nbrs:
        aggregated[0] += node_features[nbr][0]
        aggregated[1] += node_features[nbr][1]

    aggregated = [x / len(nbrs) for x in aggregated]
    updated_features[node] = aggregated

print("Updated Node Features After Graph Convolution Concept:")
for node, features in updated_features.items():
    print(f"{node} -> {features}")
