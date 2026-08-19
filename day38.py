
# HTTP Requests and APIs

import requests
import json

response = requests.get(
    "https://api.github.com/users/keshabkhatiwada96"
)

print(f"Status: {response.status_code}")

data = response.json()

print("Name:", data["name"])
print("Username:", data["login"])
print("Bio:", data["bio"])
print("Public Repositories:", data["public_repos"])
print("Followers:", data["followers"])
print(json.dumps(data, indent=4))