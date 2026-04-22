current_state = [0.15, -0.03, 0.08, -0.01]
predicted_noise = [0.05, -0.01, 0.03, 0.00]

denoised_state = [
    current_state[i] - predicted_noise[i]
    for i in range(len(current_state))
]

print("Current Noisy State:")
print(current_state)

print("\nPredicted Noise:")
print(predicted_noise)

print("\nDenoised State After One Reverse Step:")
print(denoised_state)
