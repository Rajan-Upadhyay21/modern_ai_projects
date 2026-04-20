message_sizes_mb = [10, 25, 50, 100]
latency_ms = [2, 4, 8, 16]

print("Communication Overhead Concept:")
for size, latency in zip(message_sizes_mb, latency_ms):
    print(f"Message Size: {size} MB -> Approx Communication Latency: {latency} ms")

print("\nConcept:")
print("As communication between workers increases, distributed training efficiency can decrease.")
