def howmanylist(l):
    count = 0
    for items in l:
        if type(items) == list:
            count = count + 1 
    return count

list1 = [1, [2,3], 4, [5,6], 7, 8, 9]
print(howmanylist(list1))