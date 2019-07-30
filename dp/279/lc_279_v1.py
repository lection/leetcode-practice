"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
=========================
直接上DP好了 本质上跟凑钱的题目一样 由平方数组成钱币的面额
时间复杂度 n*log(n)
========================= 超时了
似乎纯dp以python的性能无法达到了，只能考虑图搜索+剪枝了
========================= 在com站看到一个dp方案  可以勉强通过
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = min(dp[i-j*j] for j in range(1, 1 + int(i ** 0.5))) + 1
return dp[-1]
好像跟我的也没啥区别
==========================
经过反复测试 能通过也是运气 算了，还是考虑剪枝吧
========================== 看到超级代码 速度堪比作弊 不可思议
class Solution:
    def numSquares(self, n: int) -> int:
        while not n%4:
            n = int(n/4)
        if n%8==7:
            return 4
        for i in range(int(n**0.5)+1):
            j = int((n-i*i)**0.5)
            if n == i**2+j**2:
                m = 0 if not i else 1
                n = 0 if not j else 1
                return m+n
        return 3
"""


class Solution:
    def numSquares(self, n: int) -> int:
        if n < 0:
            return -1
        if n == 0 or n == 1:
            return 1

        sl = [1]
        _i = 2
        _t = 4
        while _t <= n:
            sl.append(_t)
            _i += 1
            _t = _i * _i

        if _t == n:
            return _t

        dp = [0, 1]
        for i in range(2, n + 1):
            r = i
            for s in sl:
                if s > i:
                    break
                r = min(r, dp[i - s])
            dp.insert(i, r + 1)
        return dp[-1]


s = Solution()
print(s.numSquares(4) == 1)
print(s.numSquares(12) == 3)
print(s.numSquares(13) == 2)
print(s.numSquares(7929) == 2)
print(s.numSquares(10000) == 1)
