import numpy as np


n = int(input("Enter the number of terms : "))
arr = np.array([], dtype=int)

for i in range(n):
    arr = np.insert(arr, len(arr), int(input("Enter the elements : ")))


print(arr[0])
