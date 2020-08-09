def sort_colour(arr):
    red = 0
    blue = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            red+=1
        elif arr[i] == 2:
            blue+=1
    return [1]*red + [2]*blue + [3]*(len(arr) - red - blue)

a = [1, 2, 3, 1, 3, 2, 1, 2, 3, 1]
print(sort_colour(a))