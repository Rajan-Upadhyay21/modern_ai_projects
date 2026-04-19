from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

data = [120, 122, 121, 125, 128, 130, 129, 133, 136, 140]
series = pd.Series(data)

model = ARIMA(series, order=(1, 1, 1))
fitted_model = model.fit()
forecast = fitted_model.forecast(steps=3)

print("Original Series:")
print(series)

print("\nForecast:")
print(forecast)
