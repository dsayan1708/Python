import numpy as py

arr = py.logspace(1, 8, num=5, base=10, dtype=int)

for elements in arr:
    print(elements)

for elements in range(len(arr)):
    print(arr[elements], end = " ")