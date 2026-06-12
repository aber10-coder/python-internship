import json
from datetime import datetime

def log_call(func):
    def wrapper(*args,**kwargs):
        time_s=datetime.now().strftime("%y-%m-%d %H:%M:%S")
        with open("log.txt","a") as f:
            f.write(
                f"{time_s} |"
                f"{func.__name__} |"
                f"args= {args}"
                f"kwargs= {kwargs}\n"
            )
        result= func(*args,**kwargs)
        return result
    return wrapper
def load_exp():
    try:
        with open("expenses.json","r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    
def save_exp(expenses):
    with open("expenses.json","w") as f:
        json.dump(expenses,f,indent=2)


@log_call
def add_exp(category,amount):
    expenses=load_exp()
    expense={
        "category" :category,
        "amount" :amount
    }
    expenses.append(expense)
    save_exp(expenses)
    print("Expense added succesfully!")
@log_call
def get_sum():
    expenses=load_exp()
    summary={}
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        summary[category]=summary.get(category,0)+amount
    return summary

@log_call
def view_all():
    expenses=load_exp()
    if(len(expenses)==0):
        print("No expense added!")
        return
    print("\n all expenses: ")
    for expense in expenses:
        print(
            f"category: {expense["category"]}",
            f"amount: {expense["amount"]}"
        )
def read_logs():
    count={}
    try:
        with open("log.txt","r") as f:
            for line in f:
                parts=line.split("|")
                function_name=parts[1].strip()
                count[function_name]=count.get(function_name,0)+1
    except FileNotFoundError:
        print("no logs exists!")
        return
    print("Function call counts:   ")

    for function_name,count in count.items():
            print(f"Function called: {function_name}- Count: {count}")


while True:
    print("\n--------MENU-------\n")
    print("1.Add expense")
    print("2.view summary")
    print("3.view all expenses")
    print("4. Read logs")
    print("5.Exit-")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        cat=input("Enter the category: ")
        amount=float(input("Enter the amount spended:"))
        add_exp(cat,amount)
    elif(ch==2):
        summ=get_sum()
        print("\n Expense summary--")
        for category,total in summ.items():
            print(f"{category}:${total}")
    elif(ch==3):
        view_all()
    elif(ch==4):
        read_logs()
    elif(ch==5):
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice!")





