
Code files:

## `data_poisoning_concept.py`

```python
training_data = [
    {"text": "good product", "label": "positive"},
    {"text": "excellent quality", "label": "positive"},
    {"text": "bad service", "label": "negative"},
    {"text": "terrible experience", "label": "negative"}
]

poisoned_sample = {"text": "excellent quality", "label": "negative"}

print("Original Training Data:")
for item in training_data:
    print(item)

print("\nPoisoned Sample Example:")
print(poisoned_sample)

print("\nConcept:")
print("A poisoned sample introduces misleading information into training data.")
