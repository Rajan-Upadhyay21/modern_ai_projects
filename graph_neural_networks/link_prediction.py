existing_edges = {("A", "B"), ("A", "C"), ("B", "D")}
candidate_edges = [("A", "D"), ("B", "C"), ("C", "D")]

scores = {
    ("A", "D"): 0.82,
    ("B", "C"): 0.76,
    ("C", "D"): 0.43
}

print("Link Prediction Scores:")
for edge in candidate_edges:
    print(f"{edge} -> {scores[edge]}")
