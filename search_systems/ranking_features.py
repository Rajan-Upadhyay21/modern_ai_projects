documents = [
    {"doc": "doc_1", "bm25": 0.84, "semantic_score": 0.79, "click_prior": 0.60},
    {"doc": "doc_2", "bm25": 0.71, "semantic_score": 0.90, "click_prior": 0.55},
    {"doc": "doc_3", "bm25": 0.77, "semantic_score": 0.82, "click_prior": 0.70}
]

for item in documents:
    item["final_score"] = (
        0.4 * item["bm25"] +
        0.4 * item["semantic_score"] +
        0.2 * item["click_prior"]
    )

print("Ranking Features and Final Scores:")
for item in sorted(documents, key=lambda x: x["final_score"], reverse=True):
    print(item)
