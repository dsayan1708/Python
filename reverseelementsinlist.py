def rev(l):
    a = []
    for items in range(len(l)):
        a.append(l[items][ : :-1])
    return a

list1 = ['Sayan', 'Dey', 'Abc']
print(rev(list1))