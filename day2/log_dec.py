def log_call(func):

    def wrapper(*args, **kwargs):
        print(f"Name of function called: {func.__name__}")
        print(f"Arguments passed: {args}")
        print(f"Key word args: {kwargs}")

        result=func(*args,**kwargs)
        return result
    return wrapper
@log_call
def add(a,b):
    return a+b

@log_call
def mult(a,b):
    return a*b

@log_call
def greet(name,age):
    print(f"Hi {name}")

print(f"sum of 10 and 20: {add(10,20)}   ")
print(f"multpiplication of 10 and 20: {mult(10,20)}   ")
greet("aber",age=20)


