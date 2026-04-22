import re

text = "Modern search systems use tokenization, ranking, and retrieval pipelines."

tokens = re.findall(r"\b[a-zA-Z]+\b", text.lower())
filtered_tokens = [token for token in tokens if len(token) > 2]

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nFiltered Tokens:")
print(filtered_tokens)
