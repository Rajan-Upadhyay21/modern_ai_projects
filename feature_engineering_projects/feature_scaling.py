from sklearn.preprocessing import StandardScaler
import pandas as pd

data = pd.DataFrame({
    "income": [40000, 50000, 60000, 70000]
})

scaler = StandardScaler()
data["income_scaled"] = scaler.fit_transform(data[["income"]])

print(data)
