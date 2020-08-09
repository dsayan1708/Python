from array import *

arr = array('i', [])
n = int(input("Enter the number of elements : "))
i = 0
j = 0
while (i < n):
    ele = int(input("Enter the elements : "))
    arr.append(ele)
    i+=1

arr.pop(2)

while (j < len(arr)):
    print(arr[j])
    j+=1
