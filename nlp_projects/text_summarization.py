text = """
Artificial intelligence is transforming many industries.
Machine learning helps systems learn patterns from data.
Deep learning is widely used in computer vision and NLP.
Large language models are now important in modern AI systems.
""".strip()

sentences = [sentence.strip() for sentence in text.split(".") if sentence.strip()]
summary = ". ".join(sentences[:2]) + "."

print("Original Text:")
print(text)

print("\nSummary:")
print(summary)
