checkpoint_info = {
    "epoch": 5,
    "global_step": 1200,
    "model_state": "saved_across_workers",
    "optimizer_state": "saved",
    "worker_count": 4
}

print("Distributed Checkpoint Information:")
for key, value in checkpoint_info.items():
    print(f"{key}: {value}")
