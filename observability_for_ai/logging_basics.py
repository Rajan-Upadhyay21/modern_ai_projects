
Code files:

## `logging_basics.py`

```python
logs = []

def log_event(level, message):
    logs.append({
        "level": level,
        "message": message
    })

log_event("INFO", "Prediction request received")
log_event("INFO", "Model inference completed")
log_event("WARNING", "Prediction confidence below threshold")

print("Logs:")
for log in logs:
    print(log)
