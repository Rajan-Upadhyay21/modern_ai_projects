lexical_scores = {
    "doc_1": 0.82,
    "doc_2": 0.65,
    "doc_3": 0.74
}

semantic_scores = {
    "doc_1": 0.76,
    "doc_2": 0.88,
    "doc_3": 0.80
}

hybrid_scores = {}

for doc_id in lexical_scores:
    hybrid_scores[doc_id] = 0.5 * lexical_scores[doc_id] + 0.5 * semantic_scores[doc_id]

print("Hybrid Search Results:")
for doc_id, score in sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{doc_id} -> {score:.4f}")
