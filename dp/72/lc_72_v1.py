"""
优化速度
尝试减少初始化的时间 将空字符串的情况用判断解决
==========================
正常的递推公式 dp[i][j] = 1 + min( fn(i-1, j), fn(i, j-1), fn(i-1, j-1) + w1[i]==w2[j]?-1:0)
但是 实际 当 w1[i] == w2[j] 的时候，相当于直接等于 dp[i-1][j-1]
ab ca => 2
ab cab => 1 当[i-1,j]的距离小于[i-1,j-1]的距离时，必然w1[i-1]==w2[j-1] 距离最多差1
abb cab => 2
这就为递归剪枝提供了可能性
==========================
用双数组优化取代m*n的数组矩阵初始化 加快速度 打败97%
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        if l1 == 0 or l2 == 0:
            return max(l1, l2)

        prev_dp = [j for j in range(l2+1)]
        cur_dp = [0] * (l2+1)

        for i in range(1, l1 + 1):
            cur_dp[0] = i
            for j in range(1, l2 + 1):
                if word1[i-1] == word2[j-1]:
                    cur_dp[j] = prev_dp[j-1]
                else:
                    cur_dp[j] = 1 + min(
                        prev_dp[j],
                        cur_dp[j-1],
                        prev_dp[j-1]
                    )
            cur_dp, prev_dp = prev_dp, cur_dp
        return prev_dp[-1]


s = Solution()
print(s.minDistance('horse', 'ros') == 3)
print(s.minDistance('intention', 'execution') == 5)
