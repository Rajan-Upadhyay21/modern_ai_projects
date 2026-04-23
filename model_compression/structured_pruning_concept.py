layers = {
    "conv_filter_1": "kept",
    "conv_filter_2": "removed",
    "conv_filter_3": "kept",
    "conv_filter_4": "removed"
}

print("Structured Pruning Concept:")
for layer, status in layers.items():
    print(f"{layer}: {status}")
