documents = [
    {"title": "Search Design", "topic": "search", "year": 2025},
    {"title": "Ranking Basics", "topic": "search", "year": 2024},
    {"title": "Vision Models", "topic": "cv", "year": 2025},
    {"title": "RAG Workflow", "topic": "llm", "year": 2026}
]

filtered = [
    doc for doc in documents
    if doc["topic"] == "search" and doc["year"] >= 2024
]

print("Metadata Search Results:")
for doc in filtered:
    print(doc)
