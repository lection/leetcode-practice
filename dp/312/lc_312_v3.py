"""
尝试DP解法 将v2的版本进行递推
最后一个戳破气球x 则0-x x-end两边打最优解 + 戳爆k 即是最后一个戳爆k的值
局部最优解推导全局最优解
故此 从单位开始进行递推 dp[left][right] = max([戳k + dp[left][k] + dp[k+1][right+1] for k in range(left, right+1)])
先从left-right长度为1开始计算
"""


class Solution:
    def maxCoins(self, nums) -> int:
        if not nums:
            return 0

        nums = [1] + nums + [1]

        length = len(nums)
        dp = [[0] * length for _ in range(length)]

        for n in range(0, len(nums) - 2):
            for left in range(1, length - n - 1):
                right = left + n
                r = 0
                lv = nums[left-1]
                rv = nums[right+1]
                for x in range(left, right+1):
                    r = max(r, nums[x] * lv * rv + dp[left][x-1] + dp[x+1][right])
                dp[left][right] = r

        return dp[1][-2]


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
