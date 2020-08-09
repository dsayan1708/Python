def max_sum_SubArray(arr):
    current_sum = 0
    max_so_far = arr[0]
    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        if max_so_far < current_sum:
            max_so_far = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_so_far

arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
print(max_sum_SubArray(arr))