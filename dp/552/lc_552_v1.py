"""
给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。

学生出勤记录是只包含以下三个字符的字符串：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。

示例 1:

输入: n = 2
输出: 8
解释：
有8个长度为2的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
只有"AA"不会被视为可奖励，因为缺勤次数超过一次。
注意：n 的值不会超过100000。
============
先暴力一次 肯定不通过，不用提交，就练练手。
还有很大剪枝和调优的空间，但是也算了吧，没必要。
"""
MOD_NUMBER = 10 ** 9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        if not n:
            return 0

        def check(s):
            a_count = 0
            l_count = 0
            for w in s:
                if w == 'A':
                    a_count += 1
                    l_count = 0
                elif w == 'L':
                    l_count += 1
                else:
                    l_count = 0
                if a_count > 1 or l_count > 2:
                    return 0
            print(s)
            return 1

        def rec(cn, s):
            if cn == 0:
                return check(s)
            nn = cn - 1
            result = rec(nn, s + ['A']) + rec(nn, s + ['L']) + rec(nn, s + ['P'])
            return result % MOD_NUMBER

        return rec(n, [])


s = Solution()
# print(s.checkRecord(1) == 3)
print(s.checkRecord(2) == 8)
# print(s.checkRecord(3) == 19)
# print(s.checkRecord(4) == 43)
