import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.DataFrame({
    "day": [1, 2, 3, 4, 5, 6, 7, 8],
    "demand": [120, 125, 130, 128, 135, 140, 145, 150]
})

X = df[["day"]]
y = df["demand"]

model = LinearRegression()
model.fit(X, y)

future_days = pd.DataFrame({"day": [9, 10, 11]})
future_forecast = model.predict(future_days)

print("Historical Data:")
print(df)

print("\nFuture Forecast:")
for day, forecast in zip(future_days["day"], future_forecast):
    print(f"Day {day}: {forecast:.2f}")
