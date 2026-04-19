from collections import Counter
import re

text = "Machine learning and artificial intelligence are changing modern software systems and data applications."

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
word_counts = Counter(words)

print("Top Keywords:")
for word, count in word_counts.most_common(5):
    print(word, "->", count)
