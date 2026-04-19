from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

news = [
    "Stock markets saw strong growth today",
    "The football team won their final match",
    "Scientists discovered a new planet",
    "Parliament passed a major bill",
]

labels = ["business", "sports", "science", "politics"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(news)

model = LogisticRegression(max_iter=200)
model.fit(X, labels)

test_articles = [
    "The senate approved the proposal",
    "The team celebrated a historic victory"
]

test_vec = vectorizer.transform(test_articles)
predictions = model.predict(test_vec)

for article, label in zip(test_articles, predictions):
    print(article, "->", label)
