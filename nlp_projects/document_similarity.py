from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Artificial intelligence helps automate tasks",
    "Machine learning and AI are closely related",
    "Football players train for big matches"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

similarity_matrix = cosine_similarity(X)

print("Document Similarity Matrix:")
print(similarity_matrix)
