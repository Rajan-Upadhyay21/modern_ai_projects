attention_scores = {
    "A": {"B": 0.7, "C": 0.3},
    "B": {"A": 1.0},
    "C": {"A": 1.0}
}

print("Graph Attention Scores:")
for node, neighbors in attention_scores.items():
    print(f"{node}:")
    for neighbor, score in neighbors.items():
        print(f"  attends to {neighbor} with weight {score}")
