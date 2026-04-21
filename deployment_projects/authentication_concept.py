api_keys = {
    "client_a": "KEY123",
    "client_b": "KEY456"
}

request_key = "KEY123"

is_authenticated = request_key in api_keys.values()

print("Request Key:", request_key)
print("Authenticated:", is_authenticated)
