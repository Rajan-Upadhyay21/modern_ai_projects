import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

data = np.array([10, 12, 14, 13, 15, 18, 20, 19, 21, 23, 25, 24], dtype="float32")

X = []
y = []

window_size = 3
for i in range(len(data) - window_size):
    X.append(data[i:i + window_size])
    y.append(data[i + window_size])

X = np.array(X)
y = np.array(y)

X = X.reshape((X.shape[0], X.shape[1], 1))

model = keras.Sequential([
    layers.LSTM(32, input_shape=(window_size, 1)),
    layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=100, verbose=0)

prediction = model.predict(X[-1:].reshape(1, window_size, 1), verbose=0)

print("Last Input Window:")
print(X[-1].flatten())

print("\nPredicted Next Value:")
print(prediction[0][0])
