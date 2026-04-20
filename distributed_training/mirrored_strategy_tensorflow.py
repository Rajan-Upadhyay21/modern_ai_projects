import tensorflow as tf

strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation="relu", input_shape=(10,)),
        tf.keras.layers.Dense(2, activation="softmax")
    ])

print("TensorFlow MirroredStrategy Concept:")
print("Number of devices in sync:", strategy.num_replicas_in_sync)
model.summary()
