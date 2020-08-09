from functools import wraps

def only_datatype_allow(datatype):
    def deco(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == datatype for arg in args]):
                return function(*args, **kwargs)
            print("Invalid Argument. Should only be of type integer !!")
        return wrapper
    return deco

@only_datatype_allow(str)
def string_join(*args):
    string = ""
    for items in args:
        string += items
    return string

print(string_join('Sayan', 'Dey'))