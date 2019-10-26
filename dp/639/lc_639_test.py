import sys
sys.setrecursionlimit(10000000)
M_N = 10 ** 9 + 7
ORD_6 = ord('6')


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        last_index = len(s) - 1

        def rec(idx, prev_num):
            if last_index < idx:
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

            r = rec(idx + 1, None)
            if c == '1' or c == '2':
                r = r + rec(idx + 1, c)
            elif c == '*':
                if idx < last_index and s[idx+1] == '0':
                    r = 2 * rec(idx + 2, None)
                else:
                    r = 9 * r + rec(idx + 1, '1') + rec(idx + 1, '2')
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
