def bs(nums, target):
    hi = len(nums) - 1
    low = 0
    while low <= hi:
        mid = low + (hi - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            hi = mid - 1
        else:
            low = mid + 1
    return None


print(bs([1, 3, 5, 7, 8], 3))
