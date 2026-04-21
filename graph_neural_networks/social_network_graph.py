social_graph = {
    "Rajan": ["Alice", "Bob"],
    "Alice": ["Rajan", "Charlie"],
    "Bob": ["Rajan"],
    "Charlie": ["Alice"]
}

print("Social Network Graph:")
for person, connections in social_graph.items():
    print(f"{person} is connected to {connections}")
