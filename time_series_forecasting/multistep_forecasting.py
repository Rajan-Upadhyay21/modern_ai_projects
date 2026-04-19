import numpy as np

data = [100, 102, 105, 107, 110, 112, 115]
window = data[-3:]

forecasts = []

for _ in range(3):
    next_value = sum(window) / len(window)
    forecasts.append(next_value)
    window.pop(0)
    window.append(next_value)

print("Initial Window:", data[-3:])
print("Next 3 Forecasts:", forecasts)
