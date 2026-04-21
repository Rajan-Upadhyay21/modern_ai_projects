import numpy as np

training_distribution = np.array([10, 12, 11, 13, 12, 14, 11, 13])
production_distribution = np.array([18, 20, 19, 21, 22, 20, 19, 23])

train_mean = training_distribution.mean()
prod_mean = production_distribution.mean()
mean_drift = abs(prod_mean - train_mean)

print("Training Mean:", train_mean)
print("Production Mean:", prod_mean)
print("Mean Drift:", mean_drift)

if mean_drift > 5:
    print("Drift Alert: Significant distribution shift detected.")
else:
    print("No significant drift detected.")
