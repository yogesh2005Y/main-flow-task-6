def kadane(arr):
    max_so_far = max_end = arr[0]
    for x in arr[1:]:
        max_end = max(x, max_end + x)
        max_so_far = max(max_so_far, max_end)
    return max_so_far

arr = list(map(int, input("Enter integer array: ").split()))
print("Max contiguous subarray sum:", kadane(arr))
