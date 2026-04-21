
Code files:

## `graph_representation.py`

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

print("Graph Representation:")
for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")
