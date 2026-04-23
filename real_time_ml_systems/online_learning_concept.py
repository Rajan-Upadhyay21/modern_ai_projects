model_state = {"weight": 0.5, "bias": 0.1}
new_feedback = [
    {"feature": 1.0, "label": 1},
    {"feature": 0.2, "label": 0},
    {"feature": 0.8, "label": 1}
]

print("Online Learning Concept:")
print("Initial Model State:", model_state)

for feedback in new_feedback:
    model_state["weight"] += 0.01 * feedback["feature"]
    model_state["bias"] += 0.01 * feedback["label"]

print("Updated Model State:", model_state)
