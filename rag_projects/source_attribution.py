answer = "RAG improves AI answers by retrieving external context before generation."

sources = [
    {"source_id": "doc_12", "title": "RAG Introduction"},
    {"source_id": "doc_19", "title": "Grounded Generation Notes"}
]

print("Answer:")
print(answer)

print("\nSources:")
for source in sources:
    print(f"{source['source_id']} - {source['title']}")
