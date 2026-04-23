layers = {
    "embedding": "float32",
    "linear_1": "int8",
    "linear_2": "int8",
    "output_layer": "float32"
}

print("Dynamic Quantization Concept:")
for layer, precision in layers.items():
    print(f"{layer}: {precision}")
