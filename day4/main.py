from pydantic import BaseModel, ValidationError


class TaskModel(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False


class TaskNotFoundError(Exception):
    pass


tasks = {}
next_id = 1


def get_all_tasks() -> list:
    return list(tasks.values())


def get_task(id: int) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    return tasks[id]


def create_task(data: dict) -> dict:
    global next_id

    task = TaskModel(**data)

    tasks[next_id] = task.model_dump()

    next_id += 1

    return tasks[next_id - 1]


def update_task(id: int, data: dict) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    task = TaskModel(**data)

    tasks[id] = task.model_dump()

    return tasks[id]


def delete_task(id: int) -> bool:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    del tasks[id]

    return True


while True:
    print("\n1. View All Tasks")
    print("2. View Task")
    print("3. Create Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            print(get_all_tasks())

        elif choice == "2":
            task_id = int(input("Enter task ID: "))
            print(get_task(task_id))

        elif choice == "3":
            data = {
                "title": input("Title: "),
                "priority": input("Priority: ") or "low",
                "completed": input("Completed (True/False): ").lower() == "true"
            }

            print(create_task(data))

        elif choice == "4":
            task_id = int(input("Enter task ID: "))

            data = {
                "title": input("Title: "),
                "priority": input("Priority: ") or "low",
                "completed": input("Completed (True/False): ").lower() == "true"
            }

            print(update_task(task_id, data))

        elif choice == "5":
            task_id = int(input("Enter task ID: "))

            delete_task(task_id)

            print("Task deleted.")

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

    except TaskNotFoundError as e:
        print(e)

    except ValidationError as e:
        print(e)

    except ValueError:
        print("Invalid input.")