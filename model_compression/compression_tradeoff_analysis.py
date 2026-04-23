tradeoff = {
    "original_accuracy": 0.94,
    "compressed_accuracy": 0.90,
    "original_latency_ms": 120,
    "compressed_latency_ms": 45
}

print("Compression Trade-Off Analysis:")
for key, value in tradeoff.items():
    print(f"{key}: {value}")
