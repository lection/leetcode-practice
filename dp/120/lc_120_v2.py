"""
dp 实现 直接用原数据当dp 也很简单
"""


class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0

        for level in range(len(triangle) - 2, -1, -1):
            row = triangle[level]
            next_row = triangle[level + 1]
            for idx in range(len(row)):
                row[idx] += min(next_row[idx], next_row[idx + 1])

        return triangle[0][0]


s = Solution()
print(s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]) == 11)
