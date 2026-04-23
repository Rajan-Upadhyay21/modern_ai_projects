
Code files:

## `pruning_concept.py`

```python
original_parameters = 1000000
pruned_parameters = 650000

reduction = original_parameters - pruned_parameters
reduction_percent = (reduction / original_parameters) * 100

print("Pruning Concept:")
print("Original Parameters:", original_parameters)
print("Remaining Parameters After Pruning:", pruned_parameters)
print("Removed Parameters:", reduction)
print("Reduction Percentage:", reduction_percent)
