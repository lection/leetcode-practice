"""
直接DP 初步想法是 dp存储边长 i,j = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
正方形 想想这个公式应该没问题
"""


class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        r = 0

        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                r = 1

        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                r = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                v = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                r = max(r, v)
                dp[i][j] = v

        return r * r


s = Solution()
print(s.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(s.maximalSquare([["1"]]))
print(s.maximalSquare([["0"]]))
