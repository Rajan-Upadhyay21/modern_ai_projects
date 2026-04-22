import numpy as np

training_feature = np.array([10, 12, 11, 13, 12, 14, 11, 13])
production_feature = np.array([17, 19, 18, 20, 21, 19, 18, 22])

training_mean = training_feature.mean()
production_mean = production_feature.mean()
drift = abs(production_mean - training_mean)

print("Training Feature Mean:", training_mean)
print("Production Feature Mean:", production_mean)
print("Mean Drift:", drift)
