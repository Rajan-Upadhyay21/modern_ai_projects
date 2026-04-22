unconditional_score = 0.45
conditional_score = 0.80
guidance_scale = 2.0

guided_score = unconditional_score + guidance_scale * (conditional_score - unconditional_score)

print("Unconditional Score:", unconditional_score)
print("Conditional Score:", conditional_score)
print("Guidance Scale:", guidance_scale)
print("Guided Score:", guided_score)
