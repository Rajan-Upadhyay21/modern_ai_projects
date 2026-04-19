import numpy as np
import pandas as pd

data = [100, 102, 101, 103, 105, 160, 104, 106, 107, 108]
series = pd.Series(data)

mean = series.mean()
std = series.std()

z_scores = (series - mean) / std
anomalies = series[np.abs(z_scores) > 2]

print("Series:")
print(series)

print("\nZ-Scores:")
print(z_scores)

print("\nAnomalies:")
print(anomalies)
