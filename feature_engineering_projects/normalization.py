from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.DataFrame({
    "score": [10, 20, 30, 40]
})

scaler = MinMaxScaler()
data["score_normalized"] = scaler.fit_transform(data[["score"]])

print(data)
