def min_diff(arr):
    arr=sorted(arr)
    x = len(arr)
    min_diff = 9999*9999
    for i in range(x-1):
        if(arr[i+1]-arr[i]<min_diff):
            min_diff = arr[i+1] - arr[i]
        return min_diff

arr = [1, 6, 8, 4, 5, 3, 98, 65]
print(min_diff(arr))