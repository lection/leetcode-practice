"""
尝试优化dp缓存 节省内存
当i满足2两位密码条件时
如果 i+1是满足两位密码条件，则 r = r + r/2
如果 i+1是0，则 r = r
如果 i+1是其他，则 r = r*2

2222 尝试一下 1 2 3 2+3=5 我这个规律好像不对
=====================
0真的很讨厌 我现在的思路是 0以及0前面的一位，二者均可消去
=====================
先试试两个变量比较容易实现 而且代码好看 一个变量再想办法
=====================
奇怪了，我就用了两个变量，居然内存还是只打败了 5%。
"""
ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        last_index = len(s) - 1

        def check(idx):
            if idx >= last_index:
                return False
            tl = s[idx]
            nl = s[idx + 1]
            return tl == '1' or (tl == '2' and ord(nl) <= ORD_6)

        r1 = 1
        r2 = 1
        for i in range(len(s) - 1, -1, -1):
            letter = s[i]
            if letter == '0':
                prev_letter = s[i-1]
                if prev_letter != '1' and prev_letter != '2':
                    return 0
                r1, r2 = 0, r1
                continue
            if check(i):
                r1, r2 = r1 + r2, r1
            else:
                r1, r2 = r1, r1

        return r1


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
