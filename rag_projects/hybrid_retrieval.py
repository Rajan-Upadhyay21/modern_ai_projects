semantic_scores = {
    "doc_1": 0.91,
    "doc_2": 0.84,
    "doc_3": 0.77
}

keyword_scores = {
    "doc_1": 0.60,
    "doc_2": 0.90,
    "doc_3": 0.40
}

hybrid_scores = {}

for doc_id in semantic_scores:
    hybrid_scores[doc_id] = 0.7 * semantic_scores[doc_id] + 0.3 * keyword_scores[doc_id]

ranked_docs = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)

print("Hybrid Retrieval Scores:")
for doc_id, score in ranked_docs:
    print(doc_id, "->", round(score, 4))
