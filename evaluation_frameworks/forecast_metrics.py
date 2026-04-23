from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

actual = np.array([100, 105, 110, 120])
predicted = np.array([102, 104, 111, 118])

mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
mape = np.mean(np.abs((actual - predicted) / actual)) * 100

print("Forecast Metrics:")
print("MAE:", mean_absolute_error(actual, predicted))
print("RMSE:", rmse)
print("MAPE:", mape)
