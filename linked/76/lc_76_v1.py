"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
=================
凭直觉，感觉只要两端向中间缩减就可以完成…… 琢磨几个测试用例，否定直觉。
貌似和DP没啥关系额 同学的分类有误
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


s = Solution()
print(s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC')
