search_terms = [
    "machine learning",
    "machine translation",
    "machine vision",
    "model evaluation",
    "model deployment"
]

prefix = "mach"
suggestions = [term for term in search_terms if term.startswith(prefix)]

print("Prefix:")
print(prefix)

print("\nAutocomplete Suggestions:")
for suggestion in suggestions:
    print(suggestion)
