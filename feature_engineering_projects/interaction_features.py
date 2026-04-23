import pandas as pd

data = pd.DataFrame({
    "feature_1": [1, 2, 3],
    "feature_2": [4, 5, 6]
})

data["interaction"] = data["feature_1"] * data["feature_2"]

print(data)
