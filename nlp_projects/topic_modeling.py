from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = [
    "football match goal team coach",
    "government election parliament policy",
    "software computer AI data model",
    "basketball player team championship",
    "senate law minister election"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(X)

feature_names = vectorizer.get_feature_names_out()

for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic {topic_idx + 1}:")
    top_words = [feature_names[i] for i in topic.argsort()[-5:]]
    print(top_words)
