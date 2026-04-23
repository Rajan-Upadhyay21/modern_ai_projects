model_info = {
    "original_precision": "float32",
    "quantized_precision": "int8",
    "applied_after_training": True
}

print("Post-Training Quantization:")
for key, value in model_info.items():
    print(f"{key}: {value}")
