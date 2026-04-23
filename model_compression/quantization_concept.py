full_precision_size_mb = 120
quantized_size_mb = 35

compression_ratio = full_precision_size_mb / quantized_size_mb

print("Quantization Concept:")
print("Full Precision Model Size (MB):", full_precision_size_mb)
print("Quantized Model Size (MB):", quantized_size_mb)
print("Compression Ratio:", compression_ratio)
