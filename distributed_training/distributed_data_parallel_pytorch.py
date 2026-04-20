import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(10, 32),
    nn.ReLU(),
    nn.Linear(32, 2)
)

print("PyTorch DDP Concept:")
print("Model created successfully.")

if torch.cuda.is_available():
    print("CUDA available. In real DDP, model would be wrapped with DistributedDataParallel.")
else:
    print("CUDA not available. This is a conceptual local example.")

print(model)
