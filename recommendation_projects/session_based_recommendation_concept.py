session = ["homepage", "electronics", "laptops", "gaming_laptops"]

next_item_candidates = {
    "gaming_mouse": 0.82,
    "laptop_bag": 0.74,
    "mechanical_keyboard": 0.88
}

ranked_candidates = sorted(next_item_candidates.items(), key=lambda x: x[1], reverse=True)

print("Current Session:")
print(session)

print("\nNext Item Recommendations:")
for item, score in ranked_candidates:
    print(f"{item} -> {score}")
