"""
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
==================
默认的n^2肯定是不行
子区间的和 sum(i, j) = sum(0,j) - sum(0,i)
累加子数组的和 然后利用二分查找定位复合条件的下标 时间复杂度可以控制在 n * log(n)
代码可以优化成一次遍历 累加和 搜索子数组范围 插入
============
要注意重复元素的问题 当有若干重复值的时候 有点儿麻烦
============
网上有个算法比我快一倍 研究研究
============
知道了 使用了系统自带的二分库 v2版本试试看效率是否有所提高
"""


class Solution:

    def lower(self, nums, value):
        if not nums:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        return low - 1 if nums[low - 1] == value else low

    def upper(self, nums, value):
        if not nums:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= value:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        if not nums:
            return 0
        vs = nums[0]
        vs_list = [vs]
        result = 1 if lower <= vs <= upper else 0
        for i in range(1, len(nums)):
            n = nums[i]
            vs += n
            lower_index = self.lower(vs_list, vs - lower)
            upper_index = self.upper(vs_list, vs - upper)
            if lower_index < len(vs_list) and vs_list[lower_index] == vs - lower:
                lower_index += 1
            if upper_index < lower_index:
                result += (lower_index - upper_index)
            result += 1 if lower <= vs <= upper else 0
            vs_list.insert(self.lower(vs_list, vs), vs)
        return result


s = Solution()
print(s.countRangeSum([-2, 5, -1], -2, 2) == 3)
print(s.countRangeSum([0, 0], 0, 0) == 3)
print(s.countRangeSum([-1, 1], 0, 0) == 1)
print(s.countRangeSum([2147483647, -2147483648, -1, 0], -1, 0) == 4)
# print(s.upper([0, 0, 0], 1))
# print(s.upper([0, 2, 2, 5], 3))
# print(s.lower([-2, 0, 0, 5], 0))
# print(s.upper([-2, 0, 0, 5], 0))
