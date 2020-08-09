from functools import wraps

def allow_only_int(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg) == int)
        # if all(data_types):
        #     return func(*args, **kwargs)
        # else:
        #     print("Invalid Argument. Should only be of type integer !!")
        if all([type(arg) == int for arg in args]):
            return func(*args, **kwargs)
        print("Invalid Argument. Should only be of type integer !!")
    return wrapper

@allow_only_int
def add_all(*args):
    total = 0
    for items in args:
        total+=items
    return total

print(add_all(1, 2, 3.2, 4.9, [1, 2, 3, 4]))