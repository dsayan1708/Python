def power(y):
    def of(x):
        return x**y
    return of

var = power(3)
print(var(3))