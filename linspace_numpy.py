import numpy as py

arr = py.linspace(1, 8, num=5, dtype=int, endpoint=False)

for items in arr:
    print(items)

for items in range(len(arr)):
    print(arr[items])