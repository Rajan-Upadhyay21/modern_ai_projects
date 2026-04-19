
Code files:

## `text_classification.py`

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [
    "The team won the championship match",
    "The election results were announced today",
    "The new smartphone was launched this week",
    "The player scored two goals in the game",
    "The government introduced a new policy",
    "A new software update is now available"
]

labels = ["sports", "politics", "technology", "sports", "politics", "technology"]

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.3, random_state=42
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
