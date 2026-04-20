users = {
    "admin_user": "admin",
    "analyst_user": "analyst",
    "guest_user": "guest"
}

resource_access = {
    "admin": ["model_logs", "predictions", "configurations"],
    "analyst": ["predictions"],
    "guest": []
}

username = "analyst_user"
role = users[username]
allowed_resources = resource_access[role]

print("Username:", username)
print("Role:", role)
print("Allowed Resources:", allowed_resources)
