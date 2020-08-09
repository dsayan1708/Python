def find_sum_arr(arr, sum):
    arr.sort()
    left = 0
    right = len(arr)-1
    while(left <= right):
        if(arr[left]+arr[right]>sum):
            right-=1
        elif(arr[left]+arr[right]<sum):
            left+=1
        elif(arr[left]+arr[right]==sum):
            print(f"Values of pairs are {arr[left]} and {arr[right]}")
            left+=1
            right-=1

a = [5, 7, 9, 4, 6, 3, 2, 8]
s = 7
find_sum_arr(a, s)
