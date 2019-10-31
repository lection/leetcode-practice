"""
给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

示例:

输入: matrix = [[1,0,1],[0,-2,3]], k = 2
输出: 2
解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。

说明：
矩阵内的矩形区域面积必须大于 0。
如果行数远大于列数，你将如何解答呢？
===============
穷举肯定能做，穷举可以在计算过程中优化，避免重复计算，不过似乎和DP没什么关系。
矩形的移动和扩展，都可以利用之前计算的矩形的和，所以先用回溯的手段计算矩形，然后进行右和下的移动，还有长宽的扩展。
=============== 审题错了，是矩形不是正方形，尴尬。
=============== 超时了 缓存优化 需要一个m^2*n^2 的缓存
=============== 还是超时了 此路不通 换方案
"""

class Solution:
    def maxSumSubmatrix(self, matrix, k) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        min_result = -1000000
        cache = [[[[None for _ in range(cols)] for _ in range(cols)] for _ in range(rows)] for _ in range(rows)]

        def rec(area, row, col, height, width):
            below_area = below_rec_area = below_ext_area = below_ext_rec_area = area
            right_area = right_rec_area = right_ext_area = right_ext_rec_area = area
            if cache[row][row + height - 1][col][col + width - 1] is not None:
                return cache[row][row + height - 1][col][col + width - 1]

            if row + height < rows:
                below_inc = 0
                new_row_idx = row + height
                for i in range(width):
                    below_inc += matrix[new_row_idx][col + i]
                    below_area -= matrix[row][col + i]
                below_area += below_inc
                below_rec_area = rec(below_area, row + 1, col, height, width)
                below_ext_area += below_inc
                below_ext_rec_area = rec(below_ext_area, row, col, height + 1, width)

            if col + width < cols:
                right_inc = 0
                new_col_idx = col + width
                for i in range(height):
                    right_inc += matrix[row + i][new_col_idx]
                    right_area -= matrix[row + i][col]
                right_area += right_inc
                right_rec_area = rec(right_area, row, col + 1, height, width)
                right_ext_area += right_inc
                right_ext_rec_area = rec(right_ext_area, row, col, height, width + 1)

            area = max(map(lambda x: x if x <= k else min_result,
                           (area, below_area, below_rec_area, below_ext_area, below_ext_rec_area,
                            right_area, right_rec_area, right_ext_area, right_ext_rec_area)))

            cache[row][row + height - 1][col][col + width - 1] = area
            return area

        return rec(matrix[0][0], 0, 0, 1, 1)
