import requests
url="https://api.github.com/users/octocat "
response=requests.get(url)
data=response.json()
print(f"name: {data['name']}")
print(f"location: {data['location']}")
print(f"public_repositary: {data['public_repos']}")
print(f"created_at- {data['created_at']}")