worker_gradients = [
    [0.10, 0.20, 0.30],
    [0.12, 0.18, 0.28],
    [0.11, 0.19, 0.31]
]

avg_gradient = [
    sum(grad[i] for grad in worker_gradients) / len(worker_gradients)
    for i in range(len(worker_gradients[0]))
]

print("Worker Gradients:")
for idx, grad in enumerate(worker_gradients, start=1):
    print(f"Worker {idx}: {grad}")

print("\nSynchronized Average Gradient:")
print(avg_gradient)
