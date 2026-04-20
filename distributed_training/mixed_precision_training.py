import tensorflow as tf

policy = tf.keras.mixed_precision.Policy("mixed_float16")
tf.keras.mixed_precision.set_global_policy(policy)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu", input_shape=(8,)),
    tf.keras.layers.Dense(2, activation="softmax", dtype="float32")
])

print("Mixed Precision Training:")
print("Global policy:", tf.keras.mixed_precision.global_policy())
model.summary()
