import pandas as pd

data = [12, 14, 15, 13, 16, 18, 19, 17, 20, 22]
series = pd.Series(data)

rolling_mean = series.rolling(window=3).mean()
rolling_std = series.rolling(window=3).std()

print("Original Series:")
print(series)

print("\nRolling Mean:")
print(rolling_mean)

print("\nRolling Standard Deviation:")
print(rolling_std)
