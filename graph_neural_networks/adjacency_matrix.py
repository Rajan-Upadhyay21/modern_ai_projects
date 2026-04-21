import numpy as np

nodes = ["A", "B", "C", "D"]
adj_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])

print("Nodes:")
print(nodes)

print("\nAdjacency Matrix:")
print(adj_matrix)
