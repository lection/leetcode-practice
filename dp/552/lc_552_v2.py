"""
尝试 DP 解决问题
暂时思考 状态分两组 无A和有A 每组各有三种 P L LL
L和LL是本次如果是L，是第一个连续的L还是已经是两个连续的L。
每一组的计算
本组 上组
P = P+L+LL
L = P
LL = L
单个A的出现效果和P相同，都不影响L的连续，所以加到P上。
有A组P还要加上本组无A组计算结果的P,未做本组座位A的情况。
(无A组P,无A组L,无A组LL, 有A组P, 有A组L, 有A组LL)
最终结果就是dp求和 历史出现A和不出现的 P L LL 加和 以及本次是A的情况
=================
完美通过 优化一下，去掉tuple的构建过程，直接用6变量替代。参考v3版本。
"""
MOD_NUMBER = 10 ** 9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        if not n:
            return 0

        dp = (1, 1, 0, 1, 0, 0)
        for i in range(1, n):
            p = dp[0] + dp[1] + dp[2]
            dp = (
                p % MOD_NUMBER,
                dp[0],
                dp[1],
                (dp[3] + dp[4] + dp[5] + p) % MOD_NUMBER,
                dp[3],
                dp[4],
            )

        return sum(dp) % MOD_NUMBER


s = Solution()
print(s.checkRecord(1) == 3)
print(s.checkRecord(2) == 8)
print(s.checkRecord(3) == 19)
print(s.checkRecord(4) == 43)
