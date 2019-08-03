"""
尝试官方DP思路
非常标准的DP玩法 缓存数组记录当前节点迭代至目前所在的有效括号最长长度
迭代过程出现左括号dp必然为0
右括号则有以下两种情况

一对相邻的有效左右括号
if i==')' and (i-1)=='('
    dp[i] = dp[i-2]+2

两个相邻的有括号 ....)) 形式
此时如果第一个)有对应的值 则其对应的左括号-1如果也是左括号 则说明该右括号有效 可以+2 并累加之前的dp
if i==')' and (i-1)==')' and (i-dp[i-1]-1)=='(:
    dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2

时间复杂度O(n)
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * len(s)
        result = 0

        for i in range(1, len(s)):
            if s[i] == '(':
                continue

            if s[i] == ')' and s[i-1] == '(':
                if i > 1:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2

            elif dp[i-1] != 0:
                left_idx = i - dp[i-1] - 1
                if left_idx < 0 or s[left_idx] != '(':
                    continue
                dp[i] = 2 + dp[i-1]
                if left_idx > 1:
                    dp[i] += dp[left_idx - 1]

            result = max(result, dp[i])

        return result


s = Solution()
print(s.longestValidParentheses("(()") == 2)
print(s.longestValidParentheses(")()())") == 4)
print(s.longestValidParentheses("(") == 0)
print(s.longestValidParentheses("()(())") == 6)
