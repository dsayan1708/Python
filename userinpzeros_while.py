import numpy as py 
n = int(input("Enter the number of elements : "))
arr = py.zeros(n, dtype=int)
i = 0
while(i<n):
    a = int(input("Enter the elements : "))
    arr[i] = a
    i+=1

print(arr)