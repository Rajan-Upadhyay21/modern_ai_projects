import pandas as pd

data = [100, 105, 110, 120, 125, 130, 140, 145, 150, 160]
series = pd.Series(data)

train = series[:7]
test = series[7:]

print("Train Series:")
print(train)

print("\nTest Series:")
print(test)
