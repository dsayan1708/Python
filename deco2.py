from functools import wraps
import time
def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"You are running {func.__name__} function")
        t1 = time.time()
        returned = func(*args, **kwargs) 
        t2 = time.time()
        total = t2 - t1
        print(f"This function took {total} seconds to run")
        return returned
    return wrapper

@calculate_time
def squares(l):
    return[items**2 for items in range(1, l+1)]

print(squares(10000))