def odd_even(l):
    whole = []
    odd = []
    even = []
    for items in l:
        if items % 2 == 0:
            even.append(items)
        else:
            odd.append(items)
    whole = [odd, even]
    return whole

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_even(list1))