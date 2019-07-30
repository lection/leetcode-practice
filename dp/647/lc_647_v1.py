"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
===========================
初步思路 字符串单字必然是回文
一个回文如果左右相等，则又是一个回文，所以可以用递归的思路下探。
只要下探单字和双字的所有结果即可
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        result = len(s)

        def drill(start, end):
            if start < 0 or end >= len(s) or s[start] != s[end]:
                return 0

            return 1 + drill(start - 1, end + 1)

        for i in range(len(s) - 1):
            result += drill(i, i+1) + drill(i, i+2)

        return result


s = Solution()
print(s.countSubstrings('abc') == 3)
print(s.countSubstrings('aaa') == 6)
