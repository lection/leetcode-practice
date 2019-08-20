"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
==================================
老套路 先回溯
==================================
0给我造成了一定的困扰 其实可以过滤掉所有0
==================================
用例中有一个隐藏的规则，就是无效的数字出现就是解码失败 比如 01 太烦人
总算过了。。。。居然只打败了5%。。。。
"""
ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        last_index = len(s) - 1

        cache = [0] * len(s)

        def rec(idx):
            if idx > last_index:
                return 1
            if idx == last_index:
                return 0 if s[idx] == '0' else 1

            if not cache[idx]:
                letter = s[idx]
                if letter == '0':
                    return 0
                r = rec(idx + 1)
                if letter == '1' or (letter == '2' and ord(s[idx+1]) <= ORD_6):
                    r += rec(idx + 2)
                cache[idx] = r

            return cache[idx]

        return rec(0)


s = Solution()
print(s.numDecodings('12') == 2)
print(s.numDecodings('10') == 1)
print(s.numDecodings('01') == 0)
print(s.numDecodings('0') == 0)
print(s.numDecodings('000') == 0)
print(s.numDecodings('071') == 0)
print(s.numDecodings('226') == 3)
