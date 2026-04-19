from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

messages = [
    "Win a free lottery now",
    "Claim your prize today",
    "Meeting scheduled for tomorrow",
    "Please review the attached report",
    "Earn money quickly from home",
    "Team discussion at 4 PM"
]

labels = [1, 1, 0, 0, 1, 0]

X_train, X_test, y_train, y_test = train_test_split(
    messages, labels, test_size=0.3, random_state=42
)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
