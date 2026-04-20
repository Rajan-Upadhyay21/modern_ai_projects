def receive_query(query):
    return f"Received query: {query}"

def retrieve_documents(query):
    return [
        "Company policy document chunk",
        "Internal knowledge base chunk"
    ]

def build_context(documents):
    return "\n".join(documents)

def generate_answer(query, context):
    return f"Answer for '{query}' using context:\n{context}"

user_query = "What is the company leave policy?"

print(receive_query(user_query))

documents = retrieve_documents(user_query)
context = build_context(documents)
answer = generate_answer(user_query, context)

print("\nRetrieved Documents:")
for doc in documents:
    print(doc)

print("\nFinal Answer:")
print(answer)
