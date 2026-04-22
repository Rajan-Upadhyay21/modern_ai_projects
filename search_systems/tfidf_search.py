from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "machine learning improves search systems",
    "search systems use indexing and ranking",
    "ranking models improve retrieval quality"
]

query = ["search ranking"]

vectorizer = TfidfVectorizer()
doc_matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

scores = cosine_similarity(query_vector, doc_matrix)[0]

print("TF-IDF Search Results:")
for doc, score in sorted(zip(documents, scores), key=lambda x: x[1], reverse=True):
    print(f"{doc} -> {score:.4f}")
