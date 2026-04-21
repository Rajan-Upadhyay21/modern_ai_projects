user_item_graph = {
    "User1": ["ItemA", "ItemB"],
    "User2": ["ItemB", "ItemC"],
    "User3": ["ItemA", "ItemC", "ItemD"]
}

print("Recommendation Graph Concept:")
for user, items in user_item_graph.items():
    print(f"{user} interacted with {items}")
