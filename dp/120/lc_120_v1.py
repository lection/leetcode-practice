"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
==================
回溯没啥难度 加个缓存就行了
"""


class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0

        level_count = len(triangle)
        cache = [[None] * len(row) for row in triangle]

        def rec(level, idx):
            if level >= level_count:
                return 0

            if cache[level][idx] is not None:
                return cache[level][idx]
            r = triangle[level][idx]
            next_level = level + 1
            r += min(rec(next_level, idx), rec(next_level, idx + 1))

            cache[level][idx] = r
            return r

        return rec(0, 0)


s = Solution()
print(s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]) == 11)
