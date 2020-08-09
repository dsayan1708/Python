# def reverse_list(l):
#     l.reverse()
#     # # return l
# def reverse_list(l):
#     s = l[::-1]
#     return s
def reverse_list(l):
    a = []
    for items in range(len(l)):
        s = l.pop()
        a.append(s) 
    return a

numbers = [1, 2, 3, 4]
print(reverse_list(numbers))