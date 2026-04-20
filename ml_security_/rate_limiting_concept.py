request_counts = {
    "user_1": 3,
    "user_2": 12
}

request_limit = 10

for user, count in request_counts.items():
    print(f"{user} made {count} requests")
    if count > request_limit:
        print("Rate limit exceeded")
    else:
        print("Within allowed limit")
    print("-" * 30)
