"""
一个想法 按数据首位排序 然后就可以将相邻的进行合并了
[1, 5] [3, 10] [15, 20]
只要比较 首位是否在上一个排序位的
练练手 排序就手写快排吧
轻松通过 虽然只打败 50% 但是跟第一其实差距不大
只要自己实现的快排改成官方的sorted就有质的飞跃
"""


class Solution:
    def merge(self, intervals):
        if not intervals:
            return None

        def quick(left, right):
            if left >= right:
                return
            pivot_idx = partition(left, right)
            quick(left, pivot_idx - 1)
            quick(pivot_idx + 1, right)

        def extract_pivot(left, right):
            idx = left + (right - left) // 2
            intervals[idx], intervals[right] = intervals[right], intervals[idx]

        def partition(left, right):
            extract_pivot(left, right)
            pivot = intervals[right][0]
            idx = left
            for i in range(left, right):
                if intervals[i][0] < pivot:
                    intervals[idx], intervals[i] = intervals[i], intervals[idx]
                    idx += 1
            intervals[idx], intervals[right] = intervals[right], intervals[idx]
            return idx

        quick(0, len(intervals) - 1)

        last = intervals[0]
        result = [last]
        for i in range(1, len(intervals)):
            a = intervals[i]
            if a[0] <= last[1]:
                last[1] = max(a[1], last[1])
            else:
                result.append(a)
                last = a
        return result


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(s.merge([[1, 4], [4, 5]]) == [[1, 5]])
