from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

y_true = np.array([3.0, 5.0, 2.5, 7.0])
y_pred = np.array([2.8, 5.3, 2.7, 6.5])

mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)

print("Regression Metrics:")
print("MAE:", mean_absolute_error(y_true, y_pred))
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2_score(y_true, y_pred))
