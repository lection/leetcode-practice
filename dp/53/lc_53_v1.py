"""
传统思路是将问题转化为 子序列和 - 子序列最小和
不过这算是 DP 吗？
=============
此题还有迷之 分治解法
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0

        cur_sum = 0
        min_sum = 0
        result = nums[0]
        for n in nums:
            cur_sum += n
            result = max(result, cur_sum - min_sum)
            min_sum = min(min_sum, cur_sum)

        return result
