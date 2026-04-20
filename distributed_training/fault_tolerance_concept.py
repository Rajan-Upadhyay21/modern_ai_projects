workers = {
    "worker_0": "running",
    "worker_1": "running",
    "worker_2": "failed",
    "worker_3": "running"
}

print("Fault Tolerance Concept:")
for worker, status in workers.items():
    print(f"{worker}: {status}")

print("\nConcept:")
print("Fault tolerance helps training recover or continue when one worker fails.")
