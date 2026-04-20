dataset = [f"item_{i}" for i in range(20)]
num_workers = 4

worker_splits = [dataset[i::num_workers] for i in range(num_workers)]

print("Distributed Dataloader Concept:")
for worker_id, split in enumerate(worker_splits):
    print(f"Worker {worker_id}: {split}")
