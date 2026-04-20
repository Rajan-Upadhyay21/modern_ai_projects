
Code files:

## `data_parallel_concept.py`

```python
devices = ["gpu_0", "gpu_1", "gpu_2", "gpu_3"]
batch = [f"sample_{i}" for i in range(16)]

chunks = [batch[i::len(devices)] for i in range(len(devices))]

print("Data Parallel Concept:")
for device, chunk in zip(devices, chunks):
    print(f"{device} processes: {chunk}")
