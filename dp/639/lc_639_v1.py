"""
一条包含字母 A-Z 的消息通过以下的方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
除了上述的条件以外，现在加密字符串可以包含字符 '*'了，字符'*'可以被当做1到9当中的任意一个数字。

给定一条包含数字和字符'*'的加密信息，请确定解码方法的总数。

同时，由于结果值可能会相当的大，所以你应当对10^9 + 7取模。（翻译者标注：此处取模主要是为了防止溢出）

示例 1 :

输入: "*"
输出: 9
解释: 加密的信息可以被解密为: "A", "B", "C", "D", "E", "F", "G", "H", "I".
示例 2 :

输入: "1*"
输出: 9 + 9 = 18（翻译者标注：这里1*可以分解为1,* 或者当做1*来处理，所以结果是9+9=18）
说明 :

1. 输入的字符串长度范围是 [1, 105]。
2. 输入的字符串只会包含字符 '*' 和 数字'0' - '9'。

===========================
还是先尝试从递归开始 和91差不多
很复杂……比想象的麻烦 1* *1 ** *** 都很难处理
不能再按91的递归方式去处理 要用更复杂的方式 遇到*则要看*是单独使用还是结合后面的元素组成两位数
===========================
总有新的用例让你痛不欲生
*0 让*只有1和2两种选项
*10 让*1的组合不可能出现
"""
import sys
sys.setrecursionlimit(10000000)
M_N = 10 ** 9 + 7
ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        last_index = len(s) - 1
        cache = [None] * len(s)

        def rec(idx, prev_num):
            if idx > last_index:
                return 1

            c = s[idx]

            if prev_num is not None:
                nr = rec(idx + 1, None)
                if prev_num == '1':
                    if c == '*':
                        return 9 * nr
                    else:
                        return nr
                if prev_num == '2':
                    if c == '*':
                        return 6 * nr
                    if ord(c) <= ORD_6:
                        return nr
                    return 0

            if c == '0':
                return 0

            if idx == last_index:
                return 9 if c == '*' else 1

            if cache[idx] is not None:
                return cache[idx]

            r = rec(idx + 1, None)
            if c == '1' or c == '2':
                r = r + rec(idx + 1, c)
            elif c == '*':
                if idx < last_index and s[idx+1] == '0':
                    r = 2 * rec(idx + 2, None)
                else:
                    r = 9 * r + rec(idx + 1, '1') + rec(idx + 1, '2')

            r = r % M_N
            cache[idx] = r
            return r

        return rec(0, None)


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
