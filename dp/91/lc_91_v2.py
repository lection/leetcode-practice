"""
DP解法
轻松打败 87% 可惜内存占用较高 v3进行优化
刷两次 打败了 95%
"""
ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        dp[-2] = 0 if s[len(s) - 1] == '0' else 1

        for i in range(len(s) - 2, -1, -1):
            letter = s[i]
            if letter == '0':
                if i > 0 and s[i-1] == '0':
                    return 0
                continue

            dp[i] += dp[i+1]
            if letter == '1' or (letter == '2' and ord(s[i+1]) <= ORD_6):
                dp[i] += dp[i+2]

        return dp[0]


s = Solution()
print(s.numDecodings('12') == 2)
print(s.numDecodings('10') == 1)
print(s.numDecodings('01') == 0)
print(s.numDecodings('0') == 0)
print(s.numDecodings('00') == 0)
print(s.numDecodings('000') == 0)
print(s.numDecodings('071') == 0)
print(s.numDecodings('226') == 3)
