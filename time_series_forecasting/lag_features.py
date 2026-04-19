import pandas as pd

data = [200, 210, 205, 220, 225, 230, 240, 245]
df = pd.DataFrame({"sales": data})

df["lag_1"] = df["sales"].shift(1)
df["lag_2"] = df["sales"].shift(2)

print(df)
