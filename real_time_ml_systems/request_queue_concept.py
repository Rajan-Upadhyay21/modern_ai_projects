from queue import Queue

request_queue = Queue()

requests = [
    {"request_id": "req_1", "payload": [1.0, 2.0]},
    {"request_id": "req_2", "payload": [0.5, 1.5]},
    {"request_id": "req_3", "payload": [0.8, 1.8]}
]

for request in requests:
    request_queue.put(request)

print("Request Queue Processing:")
while not request_queue.empty():
    item = request_queue.get()
    print("Processing:", item)
