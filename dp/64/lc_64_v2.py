"""
老套路 dp
"""


class Solution:
    def minPathSum(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        for x in range(1, len(grid)):
            grid[x][0] += grid[x-1][0]

        for y in range(1, len(grid[0])):
            grid[0][y] += grid[0][y-1]

        for x in range(1, len(grid)):
            for y in range(1, len(grid[0])):
                grid[x][y] += min(grid[x-1][y], grid[x][y-1])

        return grid[len(grid) - 1][len(grid[0]) - 1]


s = Solution()
print(s.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
