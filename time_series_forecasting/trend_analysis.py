import pandas as pd
import matplotlib.pyplot as plt

data = [50, 52, 54, 57, 60, 62, 65, 67, 70, 72]
series = pd.Series(data)

plt.figure(figsize=(8, 5))
plt.plot(series, marker="o")
plt.title("Trend Analysis")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.grid(True)
plt.show()
