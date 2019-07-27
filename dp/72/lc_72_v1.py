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
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        if l1 == 0 or l2 == 0:
            return max(l1, l2)

        dp = [[0] * l2 for _ in range(l1)]

        def fn(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            return dp[i][j]

        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i][j] = fn(i-1, j-1)
                else:
                    dp[i][j] = 1 + min(
                        fn(i-1, j),
                        fn(i, j-1),
                        fn(i-1, j-1)
                    )
        return dp[-1][-1]


s = Solution()
print(s.minDistance('horse', 'ros') == 3)
print(s.minDistance('intention', 'execution') == 5)
