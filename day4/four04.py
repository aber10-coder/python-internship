def get_or_404(collection: dict, id: int) -> dict:
    if id not in collection:
        raise Exception("404: Item not found")

    return collection[id]


tasks = {
    1: {"title": "Study"},
    2: {"title": "Gym"}
}

print(get_or_404(tasks, 1))

try:
    print(get_or_404(tasks, 5))
except Exception as e:
    print(e)