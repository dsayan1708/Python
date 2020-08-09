import numpy as np
n = int(input("Enter the number of terms : "))
a = np.zeros(n, dtype = int)
b = np.zeros(n, dtype = int)

for items in range(len(a)):
    z = int(input("Enter the elements : "))
    a[items] = z

for items in range(len(b)):
    z = int(input("Enter the elements : "))
    b[items] = z

arr = np.array([a,b])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()
