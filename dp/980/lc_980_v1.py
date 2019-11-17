"""
回溯是肯定可以的 先试试
============ 通过，不过速度很慢，仅打败 5%
似乎回溯没有什么优化空间了 似乎并没有什么缓存的可能
"""
import copy


class Solution:
    def uniquePathsIII(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        row_length = len(grid)
        col_length = len(grid[0])
        row_last = row_length - 1
        col_last = col_length - 1

        def rec(row, col, data, zero_count):
            v = data[row][col]
            if v < 0:
                return 0
            if v == 2:
                return 1 if zero_count == 0 else 0
            data = copy.deepcopy(data)
            # -zero_count 本质跟-1一样 只是调试的时候方便追踪轨迹
            data[row][col] = -zero_count
            zero_count -= 1
            result = 0
            if row < row_last:
                result += rec(row + 1, col, data, zero_count)
            if row > 0:
                result += rec(row - 1, col, data, zero_count)
            if col < col_last:
                result += rec(row, col + 1, data, zero_count)
            if col > 0:
                result += rec(row, col - 1, data, zero_count)
            return result

        start_row, start_col, start_zero_count = 0, 0, 0
        for ri in range(row_length):
            for ci in range(col_length):
                v = grid[ri][ci]
                if v == 0:
                    start_zero_count += 1
                elif v == 1:
                    start_row = ri
                    start_col = ci

        # 数据1为了简化代码 也算作一个0 故zero_count + 1
        return rec(start_row, start_col, grid, start_zero_count + 1)


s = Solution()
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2)
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4)
print(s.uniquePathsIII([[0, 1], [2, 0]]) == 0)
