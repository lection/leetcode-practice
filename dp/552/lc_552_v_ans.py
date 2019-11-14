"""
dp[a][l][i]: 前i个中出现a个A, 最后连续的L的个数为l的所有可能的记录的数量
========================================
此为网友答案，居然比我的DP快10倍，惊了，研究研究。
"""


class Solution:
    def myMatrixMulti(self, a, b):
        c = [[0] * 6 for i in range(6)]
        for i in range(6):
            for j in range(6):
                for k in range(6):
                    c[i][j] += a[i][k] * b[k][j] % 1000000007
                c[i][j] = c[i][j] % 1000000007
        return c

    def myMatrixPower(self, x, n):
        ans = [
            [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]
        ]
        while n > 0:
            if (n & 1):
                ans = self.myMatrixMulti(ans, x)
            x = self.myMatrixMulti(x, x)
            n >>= 1
        return ans

    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0
        M = [
            [1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]
        ]
        MM = self.myMatrixPower(M, n)
        ans = sum([MM[i][0] for i in range(6)]) % 1000000007
        return ans
