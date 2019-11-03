"""
在求最长子序列的问题中，可以把n^3的问题优化至O(n)，本题也可以参考类似的思路。
最长子序列计算问题的关键是 当前累加和-历史累加最小和 矩形面积亦可如此
原本 m^2*n*2的问题 在最后求最大矩形和 的步骤可以参考类似的方案 优化至 m * (m*n)
即 按列累加矩形面积 讲二维数组问题缩减为一位数组的问题
由于和有 k 这个限制，故采用二分查找 最终时间复杂度为 m * (m * n) * log(n)

为了让性能更优 尽量让 n > m 可以让log(n)更小 故如果 m > n 则翻转 matrix
"""
import bisect
bisect_left = bisect.bisect_left
insort_left = bisect.insort_left


class Solution:
    def maxSumSubmatrix(self, matrix, k) -> int:
        if not matrix:
            return 0

        row_length = len(matrix)
        col_length = len(matrix[0])
        if row_length > col_length:
            new_matrix = []
            for col_num in range(col_length):
                new_matrix.append([])
                for row_num in range(row_length):
                    new_matrix[col_num].append(matrix[row_num][col_num])
            return self.maxSumSubmatrix(new_matrix, k)

        result = -float('inf')
        for start_row in range(row_length):
            sum_list = [0] * col_length
            for row_num in range(start_row, row_length):
                row = matrix[row_num]
                bisect_list = [0, float('inf')]
                sum_value = 0
                for col_num in range(col_length):
                    sum_list[col_num] += row[col_num]
                    sum_value += sum_list[col_num]
                    target_value = sum_value - k
                    idx = bisect_left(bisect_list, target_value)
                    result = max(result, sum_value - bisect_list[idx])
                    if result == k:
                        return k
                    insort_left(bisect_list, sum_value)

        return result

