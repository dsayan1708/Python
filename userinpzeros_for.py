import numpy as np 
n = int(input("Enter the number of elements : "))
arr = np.zeros(n, dtype = int)

for items in range(n):
    a = int(input("Enter elements : "))
    arr[items] = a

print(arr)

for items in range(len(arr)):
    print(arr[items], end = " ")