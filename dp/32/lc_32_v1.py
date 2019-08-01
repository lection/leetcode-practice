"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
=================================
全子集毫无疑问能做，也毫无疑问会超时，不予考虑了。
还是从子问题推导全局最优解的方式考虑
当两个子串都合法，则他们相邻依然合法
如果一个合法串两侧个接入一堆括号则依旧合法
在想两边扩展的时候将数据记录在dp数组中
为了方便数组快速找到边界值合并 故数组中记录合法括号下标数据
例如 start end 是合法括号的下标 怎么dp[end]=start dp[start]=end
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        dp = [-1] * len(s)
        result = 0
        for i in range(len(s) - 1):
            if dp[i] != -1 or s[i] != '(' or s[i+1] != ')':
                continue

            start, end = i, i + 1

            while True:
                dp[start] = end
                dp[end] = start
                result = max(result, end - start + 1)

                if start > 0 and dp[start-1] != -1:
                    start = dp[start - 1]
                    continue

                if end < (len(s)-1) and dp[end+1] != -1:
                    end = dp[end + 1]
                    continue

                if start != 0 and end != (len(s) - 1) and s[start - 1] == '(' and s[end+1] == ')':
                    start -= 1
                    end += 1
                    continue

                break
        return result


s = Solution()
print(s.longestValidParentheses("(()") == 2)
print(s.longestValidParentheses(")()())") == 4)
