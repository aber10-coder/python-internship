import requests
url=" https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
data=response.json()
print(f"name: {data['setup']}")
print(f"location: {data['punchline']}")
