from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = [
    "deep learning neural networks AI",
    "machine learning data science model",
    "football team player goal",
    "basketball coach team game"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

model = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = model.fit_predict(X)

for doc, cluster in zip(documents, clusters):
    print(f"Cluster {cluster}: {doc}")
