num_gpus = [1, 2, 4, 8]
training_times = [100, 55, 30, 18]

baseline_time = training_times[0]

print("Scaling Efficiency:")
for gpu_count, time_taken in zip(num_gpus, training_times):
    speedup = baseline_time / time_taken
    efficiency = speedup / gpu_count
    print(f"GPUs: {gpu_count}, Time: {time_taken}, Speedup: {speedup:.2f}, Efficiency: {efficiency:.2f}")
