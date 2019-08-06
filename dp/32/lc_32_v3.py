"""
参考官方答案
顺序遍历字符串时 我们容易判断
(()))))
)))()()
这类多余的右括号 因为当左右括号数量匹配之后，直接出现的右括号是明显无效的。

难以判断的是类似以下左括号较多的情况
(((()((((()))
当左括号过多，右括号始终无法匹配全部的左括号，则会出现右括号连续有效难以判断的情况
这时只需要倒序遍历即可得到合理的答案

* 故此，最长的有效括号匹配字符串，必然会在顺序或者倒序中遇到 左右括号数量完全匹配的情况 *

只需要顺序倒序各遍历一次即可得到答案

惊人的简单高效 打败 92%

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        result = 0

        left = 0
        right = 0
        for k in s:
            if k == '(':
                left += 1
            else:
                right += 1
            if left == right:
                result = max(right, result)
            if left < right:
                left = right = 0

        left = right = 0
        for i in range(len(s)-1, -1, -1):
            k = s[i]
            if k == '(':
                left += 1
            else:
                right += 1
            if left == right:
                result = max(right, result)
            if left > right:
                left = right = 0

        return result * 2


s = Solution()
print(s.longestValidParentheses("()()") == 4)
print(s.longestValidParentheses("(()") == 2)
print(s.longestValidParentheses(")()())") == 4)
print(s.longestValidParentheses("(") == 0)
print(s.longestValidParentheses("()(())") == 6)
print(s.longestValidParentheses("()(()") == 2)
print(s.longestValidParentheses("(()(((()") == 2)
