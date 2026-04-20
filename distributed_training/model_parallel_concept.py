model_parts = {
    "gpu_0": ["embedding_layer", "encoder_block_1", "encoder_block_2"],
    "gpu_1": ["encoder_block_3", "encoder_block_4", "output_layer"]
}

print("Model Parallel Concept:")
for device, layers in model_parts.items():
    print(f"{device} holds layers: {layers}")
