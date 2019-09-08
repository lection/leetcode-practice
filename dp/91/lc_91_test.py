ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        last_index = len(s) - 1
        dp = [0] * (len(s) + 1)

        dp[-1] = 1
        if s[last_index] != '0':
            dp[-2] = 1

        for idx in range(len(s) - 2, -1, -1):
            c = s[idx]
            if c == '0':
                continue
            r = dp[idx + 1]
            if c == '1' or (c == '2' and ord(s[idx + 1]) <= ORD_6):
                r += dp[idx + 2]

            dp[idx] = r

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
print(s.numDecodings('230') == 0)
print(s.numDecodings('12120') == 3)
