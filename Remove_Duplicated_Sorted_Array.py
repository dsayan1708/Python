def remove_duplicates(arr):
    arr = sorted(arr)
    # print(arr)
    rmv_dpl = list(set(arr))
    return rmv_dpl

a = [9, 7, 5, 8, 6, 1, 2, 4, 3, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_duplicates(a))