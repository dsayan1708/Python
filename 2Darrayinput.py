import numpy as py
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
arr = py.zeros((r, c), dtype = int)

length = len(arr)

for i in range(length):
    for j in range(len(arr[i])):
        x = int(input("Enter the elements : "))
        arr[i][j] = x

for i in range((length)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print()

print(arr)
