from time import time
def timer(func):

    def wrapper():
        start_t=time()
        func()
        end_t= (time()-start_t)
        print(end_t)
    return wrapper

@timer
def counter():
    for i in range(0,1000000):
        pass
    


counter()
