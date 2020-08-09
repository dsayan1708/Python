def decorator_function(func):
    def msg():
        print("Hey...")
        func()
    return msg

@decorator_function
def deco1():
    print("This is a decorator function.")

deco1()

def deco2():
    print("This is also a decorator function")


# abc = decorator_function(deco2)
# abc()