import numpy as py

n = int(input("Enter number of elements : "))
x = []
y = []
z = []
print(type(x))

print("Enter elements for first array")
for i in range(n):
    x.append(int(input("Enter the elements : ")))

print("Enter the elements for second array")
for j in range(n):
    y.append(int(input("Enter the elements : ")))

print("Enter the elements for resultant array")
for k in range(n):
    z.append(int(input("Enter the elements : ")))


a = py.array([x, y]) 
b = py.array(z)

print(py.linalg.solve(a,b))