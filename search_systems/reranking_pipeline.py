results = [
    {"doc": "doc_1", "initial_score": 0.81, "query_overlap": 2},
    {"doc": "doc_2", "initial_score": 0.79, "query_overlap": 0},
    {"doc": "doc_3", "initial_score": 0.77, "query_overlap": 3}
]

for item in results:
    item["reranked_score"] = item["initial_score"] + 0.05 * item["query_overlap"]

reranked = sorted(results, key=lambda x: x["reranked_score"], reverse=True)

print("Reranked Results:")
for item in reranked:
    print(item)
