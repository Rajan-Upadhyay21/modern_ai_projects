from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.DataFrame({
    "grade": ["low", "medium", "high", "medium", "low"]
})

encoder = LabelEncoder()
data["grade_encoded"] = encoder.fit_transform(data["grade"])

print(data)
