from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif
import pandas as pd

X, y = load_iris(return_X_y=True)
feature_names = load_iris().feature_names

selector = SelectKBest(score_func=f_classif, k=2)
X_selected = selector.fit_transform(X, y)

selected_features = [feature_names[i] for i in selector.get_support(indices=True)]

print("Selected Features:")
print(selected_features)

print("\nSelected Feature Matrix Shape:")
print(X_selected.shape)
