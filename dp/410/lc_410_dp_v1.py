"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
==========
暴力不考虑 必然超时
好特么有难度
==========
强行DP 每个index对应m个状态，每个状态代表0-index的数据被分为m段子数组的最优解。
dp[i][j]代表 0-i的数据切分为j+1个子数组的解
状态转移方程
dp[i][j] = min( max(dp[k - 1][j], sum(nums[k: i])) for k in range(j, i))
==========
可惜也是超时了
时间复杂度是 n * m * n
貌似DP本题的极限也就是如此了 查询讨论，更建议使用二分法解决
"""
import sys
MAX_VALUE = sys.maxsize


class Solution:
    def splitArray(self, nums, m: int) -> int:
        if not nums or m <= 0:
            return 0
        dp = [[0] * m for _ in nums]
        dp[0][0] = sum_value = nums[0]

        for idx in range(1, len(nums)):
            sum_value += nums[idx]
            dp[idx][0] = sum_value
            for j in range(1, min(idx + 1, m)):
                sub_sum_value = 0
                min_value = MAX_VALUE
                j_1 = j - 1
                for k in range(idx, j_1, -1):
                    sub_sum_value += nums[k]
                    min_value = min(min_value, max(sub_sum_value, dp[k - 1][j_1]))
                dp[idx][j] = min_value

        return dp[-1][-1]


s = Solution()
print(s.splitArray([7, 2, 5, 10, 8], 2) == 18)
