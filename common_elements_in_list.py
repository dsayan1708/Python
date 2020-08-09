def common(l, m):
    a = []
    for items in l:
        if items in m:
            a.append(items)
    return a

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common(list1, list2))