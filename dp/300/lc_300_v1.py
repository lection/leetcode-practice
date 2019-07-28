"""
第一直觉 暴力全组合 必然超时
==================================
DP方案 dp[i] = 1 + max(dp[filter(x < mums[i])])
n^2 方案
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = 1 + max(
                (
                    dp[x] if nums[x] < nums[i] else 0 for x in range(i+1)
                )
            )

        return max(dp)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
