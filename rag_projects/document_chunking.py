
Code files:

## `document_chunking.py`

```python
text = """
PyTorch is a deep learning framework.
Transformers are used in modern language models.
RAG combines retrieval and generation.
Embeddings help semantic search.
Chunking improves retrieval quality.
""".strip()

lines = text.split("\n")
chunks = []
chunk_size = 2

for i in range(0, len(lines), chunk_size):
    chunk = " ".join(lines[i:i + chunk_size]).strip()
    chunks.append(chunk)

print("Chunks:")
for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}: {chunk}")
