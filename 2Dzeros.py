import numpy as py

arr = py.zeros((3,2), dtype = int)

print("Using size")

for items in arr:
    for i in items:
        print(i, end = " ")
    print()

print("Using index")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print()