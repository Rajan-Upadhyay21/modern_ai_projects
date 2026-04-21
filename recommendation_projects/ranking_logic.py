items = [
    {"item": "Item_A", "relevance": 0.82, "popularity": 0.70},
    {"item": "Item_B", "relevance": 0.76, "popularity": 0.85},
    {"item": "Item_C", "relevance": 0.91, "popularity": 0.60},
]

for item in items:
    item["final_score"] = 0.7 * item["relevance"] + 0.3 * item["popularity"]

ranked_items = sorted(items, key=lambda x: x["final_score"], reverse=True)

print("Ranked Items:")
for item in ranked_items:
    print(item)
