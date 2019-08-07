"""
我有一种可以直接上DP的错觉。
dp最后一位是0 每一个下标对应的是能查找范围中最小值+1
理论上是个n^2的时间复杂度

=========================果然超时了
如果改成自从前向后dp，倒是可以避免类似出道即巅峰的情况，但是本质似乎没什么进步。
=========================
v1版本失败
"""


class Solution:
    def jump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return 0

        length = len(nums)
        dp = [0] * length

        for i in range(length - 2, -1, -1):
            if nums[i] <= 0:
                dp[i] = length
                continue
            dp[i] = 1 + min(dp[i+1: min(i+nums[i]+1, length)])
        return dp[0]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]) == 2)
print(s.jump([2, 3, 0, 1, 4]) == 2)
