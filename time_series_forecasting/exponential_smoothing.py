from statsmodels.tsa.holtwinters import SimpleExpSmoothing
import pandas as pd

data = [100, 102, 101, 105, 107, 110, 108, 111, 115, 117]
series = pd.Series(data)

model = SimpleExpSmoothing(series).fit(smoothing_level=0.3, optimized=False)
forecast = model.forecast(3)

print("Original Series:")
print(series)

print("\nForecast:")
print(forecast)
