from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)

model = RandomForestClassifier(random_state=42)
scores = cross_val_score(model, X, y, cv=5)

print("Cross-Validation Scores:")
print(scores)
print("Mean CV Score:", scores.mean())
