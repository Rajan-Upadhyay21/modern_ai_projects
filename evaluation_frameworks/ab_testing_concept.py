model_a_click_rate = 0.18
model_b_click_rate = 0.22

print("A/B Testing Concept:")
print("Model A Click Rate:", model_a_click_rate)
print("Model B Click Rate:", model_b_click_rate)

if model_b_click_rate > model_a_click_rate:
    print("Model B performs better in this comparison.")
else:
    print("Model A performs better in this comparison.")
