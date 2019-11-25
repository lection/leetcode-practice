"""
囧 内存消耗打败的人也并没减少多少 5%
=============
试了一下自称内存击败100%的 也还是5% 罢了
可以提高速度的地方 选择插入点的地方可以用二分查找优化 先不折腾了
"""
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        idx = len(intervals)
        for i in range(len(intervals)):
            a = intervals[i]
            if a[1] >= newInterval[0]:
                idx = i
                break
        intervals.insert(idx, newInterval)

        for i in range(idx + 1, len(intervals)):
            a = intervals[idx]
            b = intervals[i]
            if a[1] < b[0]:
                idx += 1
                intervals[idx] = b
            else:
                a[0] = min(a[0], b[0])
                a[1] = max(a[1], b[1])

        return intervals[:idx + 1]


s = Solution()
# print(s.insert([[2, 5], [6, 7], [8, 9]], [0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]])
# print(s.insert([[1, 5]], [2, 3]) == [[1, 5]])
# print(s.insert([], [5, 7]) == [[5, 7]])
print(s.insert([[1, 5]], [5, 7]) == [[1, 7]])
# print(s.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]])
# print(s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
# print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
