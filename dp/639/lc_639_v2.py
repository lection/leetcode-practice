"""
尝试使用DP
太久没刷题了，忘了91题的玩法了。
暂时的思路是从末尾向前推导，只要递归做的出来，这个似乎没啥难度。
注意审题 * 只能表达1-9，不代表0，容易忘了这个要点。
还有一点是，不要一上来就想把代码写的太简洁，
像本题对于数字的各种判断有点儿复杂，但是穷举也十分有限，if else也不过十来个。
如果一开始太执着于代码简洁，企图缩减if else数量，反倒容易掉到沟里。
先写好，再简化吧。
"""
M_N = 10 ** 9 + 7
ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        # 下标 0:独立使用 1:两位数
        dp1 = 1
        dp2 = 1
        if s[-1] == '0':
            dp1 = 0
        elif s[-1] == '*':
            dp1 = 9

        last_index = len(s) - 1
        for idx in range(last_index - 1, -1, -1):
            c = s[idx]
            if c == '0':
                dp = 0
            elif c == '1':
                if s[idx + 1] == '*':
                    dp = dp1 + 9 * dp2
                else:
                    dp = dp1 + dp2
            elif c == '2':
                nc = s[idx + 1]
                if nc == '*':
                    dp = dp1 + 6 * dp2
                elif ord(nc) <= ORD_6:
                    dp = dp1 + dp2
                else:
                    dp = dp1
            elif c == '*':
                nc = s[idx + 1]
                if nc == '*':
                    dp = 9 * dp1 + 15 * dp2
                elif nc == '0':
                    dp = 2 * dp2
                elif ord(nc) <= ORD_6:
                    dp = 9 * dp1 + 2 * dp2
                else:
                    dp = 9 * dp1 + dp2
            else:
                dp = dp1

            dp = dp % M_N
            dp1, dp2 = dp, dp1

        return dp1

s = Solution()
print(s.numDecodings("*") == 9)
print(s.numDecodings("1*") == 18)
print(s.numDecodings("2*") == 15)
print(s.numDecodings("3*") == 9)
print(s.numDecodings("**") == 96)
print(s.numDecodings("*2") == 11)
print(s.numDecodings("*1") == 11)
print(s.numDecodings("***") == 999)
print(s.numDecodings("*1*1*0") == 404)
print(s.numDecodings("*0**0") == 36)
print(s.numDecodings("*10*1") == 99)
