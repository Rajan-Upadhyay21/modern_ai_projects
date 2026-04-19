import re

text = "Rajan Upadhyay studied at Roosevelt University in Chicago and worked on AI projects."

capitalized_words = re.findall(r"\b[A-Z][a-z]+\b", text)

print("Text:")
print(text)

print("\nPotential Named Entities:")
print(capitalized_words)
