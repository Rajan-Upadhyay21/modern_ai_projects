blocked_terms = ["password", "secret key", "confidential", "private token"]

generated_output = "The system password and secret key should never be exposed."

flagged = any(term in generated_output.lower() for term in blocked_terms)

print("Generated Output:")
print(generated_output)

print("\nFlagged for Filtering:")
print(flagged)
