import json
from datetime import datetime
from pydantic import BaseModel, ValidationError


# ---------------- Pydantic Model ----------------

class Expense(BaseModel):
    category: str
    amount: float


# ---------------- Decorator ----------------

def log_call(func):
    def wrapper(*args, **kwargs):
        time_s = datetime.now().strftime("%y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as f:
            f.write(
                f"{time_s} | "
                f"{func.__name__} | "
                f"args={args} | "
                f"kwargs={kwargs}\n"
            )

        result = func(*args, **kwargs)
        return result

    return wrapper


# ---------------- File Handling ----------------

def load_exp():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []


def save_exp(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)


# ---------------- Expense Functions ----------------

@log_call
def add_exp(category, amount,before):
    expenses = load_exp()

    try:
        expense = Expense(
            category=category,
            amount=amount
        )

        expenses.append(expense.model_dump())
        save_exp(expenses)

        print("Expense added successfully!")

    except ValidationError as e:
        print("\nInvalid expense data:")
        print(e)


@log_call
def get_sum():
    expenses = load_exp()

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    return summary


@log_call
def view_all():
    expenses = load_exp()

    if len(expenses) == 0:
        print("No expenses added!")
        return

    print("\nAll Expenses:")

    for expense in expenses:
        print(
            f"Category: {expense['category']}, "
            f"Amount: {expense['amount']}"
        )


def read_logs():
    count = {}

    try:
        with open("log.txt", "r") as f:
            for line in f:
                parts = line.split("|")

                function_name = parts[1].strip()

                count[function_name] = (
                    count.get(function_name, 0) + 1
                )

    except FileNotFoundError:
        print("No logs exist!")
        return

    print("\nFunction Call Counts:")

    for function_name, total in count.items():
        print(
            f"Function: {function_name} "
            f"- Count: {total}"
        )


# ---------------- Menu ----------------

while True:
    print("\n-------- MENU --------")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. View All Expenses")
    print("4. Read Logs")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        category = input("Enter the category: ")
        amount = input("Enter the amount spent: ")

        add_exp(category, amount)

    elif ch == 2:
        summary = get_sum()

        print("\nExpense Summary:")

        for category, total in summary.items():
            print(f"{category}: ${total}")

    elif ch == 3:
        view_all()

    elif ch == 4:
        read_logs()

    elif ch == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")