def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]
A = list(map(int, input("Enter sorted array A: ").split()))
B = list(map(int, input("Enter sorted array B: ").split()))
print("Median:", find_median_sorted_arrays(A,B))

