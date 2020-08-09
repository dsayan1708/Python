list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
# for items in range(n):
#     a = int(input("Enter your items : "))
#     list1.append(a)
print(list1)
for e, items in enumerate(list1):
    print(tuple((e, items), end = " "))
    # print(f"The index is {e} and the value of index is {items}")