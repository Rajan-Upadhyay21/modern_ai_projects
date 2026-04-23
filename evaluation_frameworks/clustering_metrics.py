from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=100, centers=3, random_state=42)
labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X)

score = silhouette_score(X, labels)

print("Clustering Metrics:")
print("Silhouette Score:", score)
