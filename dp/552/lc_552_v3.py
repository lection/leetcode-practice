"""
提高了800ml以内 但是距离答案还是有很大差距
"""
MOD_NUMBER = 10 ** 9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        if not n:
            return 0

        np, nl, nll, ap, al, hall = (1, 1, 0, 1, 0, 0)
        for i in range(1, n):
            p = np + nl + nll
            nll = nl
            nl = np
            np = p % MOD_NUMBER
            p = ap + al + hall
            hall = al
            al = ap
            ap = p % MOD_NUMBER + np

        return (np + nl + nll + ap + al + hall) % MOD_NUMBER


s = Solution()
print(s.checkRecord(1) == 3)
print(s.checkRecord(2) == 8)
print(s.checkRecord(3) == 19)
print(s.checkRecord(4) == 43)
print(s.checkRecord(100) == 985598218)
