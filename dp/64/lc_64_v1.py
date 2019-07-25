"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
==================================
老套路 先递归
"""


class Solution:
    def minPathSum(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        max_x = len(grid) - 1
        max_y = len(grid[0]) - 1

        cache = [[None] * len(grid[0]) for _ in range(len(grid))]

        def dfs(x, y):
            v = grid[x][y]

            sr = None

            if cache[x][y] is None:
                if x < max_x:
                    sr = dfs(x+1, y)

                if y < max_y:
                    r = dfs(x, y + 1)
                    sr = r if sr is None else min(r, sr)
                cache[x][y] = v + sr if sr is not None else 0

            return cache[x][y]

        return dfs(0, 0) + grid[max_x][max_y]


s = Solution()
print(s.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]) == 7)
