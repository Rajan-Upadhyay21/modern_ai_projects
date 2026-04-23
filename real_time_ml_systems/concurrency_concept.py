import threading
import time

def handle_request(request_id):
    print(f"Starting request {request_id}")
    time.sleep(0.5)
    print(f"Finished request {request_id}")

threads = []

for request_id in ["req_1", "req_2", "req_3"]:
    thread = threading.Thread(target=handle_request, args=(request_id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All concurrent requests completed.")
