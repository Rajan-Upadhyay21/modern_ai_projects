
Code files:

## `moving_average_forecasting.py`

```python
import pandas as pd

data = [100, 102, 101, 105, 107, 110, 108, 111, 115, 117]
series = pd.Series(data)

moving_avg = series.rolling(window=3).mean()
forecast = moving_avg.iloc[-1]

print("Original Series:")
print(series)

print("\n3-Point Moving Average:")
print(moving_avg)

print("\nNext Forecast Value:")
print(forecast)
