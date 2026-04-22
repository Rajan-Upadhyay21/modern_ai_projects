vocabulary = ["search", "system", "ranking", "retrieval", "semantic"]
query = "retrival"

def simple_correction(word, vocab):
    for candidate in vocab:
        if candidate.startswith(word[:4]):
            return candidate
    return word

corrected = simple_correction(query, vocabulary)

print("Original Query Term:")
print(query)

print("\nCorrected Term Suggestion:")
print(corrected)
