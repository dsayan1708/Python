import numpy as np

arr = []

n = int(input("Enter the number of terms : "))
for items in range(n):
    arr.append(int(input("Enter the items : ")))

print(arr)
print(type(arr))

arr = np.array(arr)

a = np.nonzero(arr)

print(a)