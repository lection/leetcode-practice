"""
与之前的dp不同之处在于
1 起点与终点不再是二维数组的第一个点与最后一个点
2 每一个0点都要遍历
"""


class Solution:
    def uniquePathsIII(self, grid) -> int:
        if not grid or not grid[0]:
            return 0


s = Solution()
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2)
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4)
print(s.uniquePathsIII([[0, 1], [2, 0]]) == 0)
