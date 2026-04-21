nodes = {
    "A": {"features": [1.0, 0.2], "label": "admin"},
    "B": {"features": [0.7, 0.5], "label": "user"},
    "C": {"features": [0.3, 0.9], "label": "user"}
}

print("Node Classification Data:")
for node, info in nodes.items():
    print(f"{node} -> {info}")
