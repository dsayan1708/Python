from functools import wraps

def print_function_data(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        print(f"You are calling {func.__name__}")
        print(f"This function {func.__doc__}")
        return func(*args, **kwargs)
    return wrapper_function

@print_function_data
def add(a, b):
    '''takes two integers as input and returns their sum as output'''
    return a+b

print(add(5,6))