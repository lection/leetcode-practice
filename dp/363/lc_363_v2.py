"""
在leetcode上了试了试 m^2 * n^2的循环，没有超时，目前考虑使用这种迭代手段。
先对原始matrix进行m*n的预计算，每个cell存放从0,0到m,n的矩形和。
matrix[m][n] = matrix[m][n] + matrix[m-1][n] + matrix[m][n-1] - matrix[m-1][n-1]

然后进行一轮m^2*n^2的迭代，遍历所有矩形，找出最大值。
矩形 m1n1m2n2 的值为
r = matrix[m2][n2] - matrix[m2][n1] - matrix[m1][n2] + matrix[m1][n1]
如果 r == k 则可以提前返回
============= 可惜在有一个更加巨大的用例面前，超时了,难道有优化成 m*n的方法？？
把 result = max(result, area) 改成 if 判断 速度略微提高 但意义不大
"""


class Solution:
    def maxSumSubmatrix(self, matrix, k) -> int:
        if not matrix:
            return 0

        row_length = len(matrix)
        col_length = len(matrix[0])

        result = -10000000
        # 预处理
        for row in range(row_length):
            for col in range(col_length):
                area = matrix[row][col]
                if row > 0:
                    area += matrix[row - 1][col]
                if col > 0:
                    area += matrix[row][col - 1]
                if row > 0 and col > 0:
                    area -= matrix[row - 1][col - 1]
                matrix[row][col] = area
        # 计算
        for r1 in range(row_length):
            for c1 in range(col_length):
                for r2 in range(r1, row_length):
                    for c2 in range(c1, col_length):
                        area = matrix[r2][c2]
                        if r2 > r1 and c2 > c1:
                            area -= matrix[r1][c2] + matrix[r2][c1] - matrix[r1][c1]
                        elif r2 > r1:
                            area -= matrix[r1][c2]
                        elif c2 > c1:
                            area -= matrix[r2][c1]
                        if area == k:
                            return k
                        if result < area < k:
                            result = area

        return result

