"""
系统库比自己写的二分查找效率高 我的二分查找有待提高
"""
import bisect


class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        if not nums:
            return 0

        vs = nums[0]
        vs_list = [vs]
        result = 1 if lower <= vs <= upper else 0
        for i in range(1, len(nums)):
            n = nums[i]
            vs += n
            lower_index = bisect.bisect_right(vs_list, vs - lower)
            upper_index = bisect.bisect_left(vs_list, vs - upper)
            if lower_index < len(vs_list) and vs_list[lower_index] == vs - lower:
                lower_index += 1
            if upper_index < lower_index:
                result += (lower_index - upper_index)
            result += 1 if lower <= vs <= upper else 0
            bisect.insort_left(vs_list, vs)
        return result


s = Solution()
print(s.countRangeSum([-2, 5, -1], -2, 2) == 3)
print(s.countRangeSum([0, 0], 0, 0) == 3)
print(s.countRangeSum([-1, 1], 0, 0) == 1)
print(s.countRangeSum([2147483647, -2147483648, -1, 0], -1, 0) == 4)
