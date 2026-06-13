import requests
from typing import Any


def fetch_user(username: str) -> dict[str, Any]:
    url: str = f"https://api.github.com/users/{username}"

    try:
        response: requests.Response = requests.get(url)
        response.raise_for_status()

        user: dict[str, Any] = response.json()
        return user

    except requests.exceptions.RequestException:
        print("Could not fetch GitHub user data.")
        return {}


def fetch_joke() -> tuple[str, str]:
    url: str = "https://official-joke-api.appspot.com/random_joke"

    try:
        response: requests.Response = requests.get(url)
        response.raise_for_status()

        joke: dict[str, Any] = response.json()

        setup: str = joke["setup"]
        punchline: str = joke["punchline"]

        return setup, punchline

    except requests.exceptions.RequestException:
        print("Could not fetch joke.")
        return "", ""


def display_user(user: dict[str, Any]) -> None:
    if not user:
        print("No user data found.")
        return

    print("\n===== GitHub User Card =====")
    print(f"Name         : {user['name']}")
    print(f"Username     : {user['login']}")
    print(f"Location     : {user['location']}")
    print(f"Public Repos : {user['public_repos']}")
    print(f"Created At   : {user['created_at']}")
    print("============================")



github_username: str = input("Enter GitHub username: ")

user: dict[str, Any] = fetch_user(github_username)

display_user(user)

setup: str
punchline: str

setup, punchline = fetch_joke()

if setup and punchline:
    print("\n===== Random Joke =====")
    print(setup)
    print(punchline)
    print("=======================")