def max_diff(arr):
    arr = sorted(arr, reverse = True)
    x = len(arr)
    max_diff = 0
    for i in range(x-1):
        if(arr[i]-arr[i+1] > max_diff):
            max_diff = arr[i] - arr[i+1]
        return max_diff

arr = [1, 6, 8, 4, 5, 3, 98, 65]
print(max_diff(arr))