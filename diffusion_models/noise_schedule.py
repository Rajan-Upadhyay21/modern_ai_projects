import numpy as np

timesteps = 10
beta_start = 0.0001
beta_end = 0.02

beta_schedule = np.linspace(beta_start, beta_end, timesteps)

print("Noise Schedule:")
print(beta_schedule)
