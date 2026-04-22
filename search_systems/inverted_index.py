
Code files:

## `inverted_index.py`

```python
from collections import defaultdict
import re

documents = {
    1: "machine learning improves search systems",
    2: "search systems use indexing and ranking",
    3: "ranking models improve retrieval quality"
}

index = defaultdict(list)

for doc_id, text in documents.items():
    terms = re.findall(r"\b\w+\b", text.lower())
    for term in set(terms):
        index[term].append(doc_id)

print("Inverted Index:")
for term, postings in sorted(index.items()):
    print(f"{term} -> {postings}")
