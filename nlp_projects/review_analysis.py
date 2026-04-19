from collections import Counter
import re

reviews = [
    "The product quality is amazing and the design is excellent",
    "Customer service was poor and the delivery was slow",
    "The design is good and the quality is great"
]

all_words = []
for review in reviews:
    words = re.findall(r"\b[a-zA-Z]+\b", review.lower())
    all_words.extend(words)

word_counts = Counter(all_words)

print("Most Common Review Terms:")
for word, count in word_counts.most_common(10):
    print(word, "->", count)
