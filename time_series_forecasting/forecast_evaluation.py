import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

actual = np.array([100, 105, 110, 120])
predicted = np.array([102, 104, 111, 118])

mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)

print("Actual:", actual)
print("Predicted:", predicted)

print("\nMAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
