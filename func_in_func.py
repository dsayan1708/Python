def square(a):
    return a**2
l = [1, 2, 3, 4, 5]

def my_map(func, n):
    sq = []
    for items in n:
        sq.append(func(items))
    return sq

print(my_map(square, l))