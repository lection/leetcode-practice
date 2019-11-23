"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
=================
直觉上n^2的方案肯定能求出解 但是可能超时
反正每一个数组都去遍历遇到能合并的就合并
这个实现没有任何意义 就是练练手
================= 果然超时
"""


class Solution:
    def merge(self, intervals):
        flag = True
        length = len(intervals)
        while flag:
            flag = False
            for i in range(length):
                if intervals[i] is None:
                    continue
                a = intervals[i]
                for j in range(length):
                    if i == j or intervals[j] is None:
                        continue
                    b = intervals[j]
                    if b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
                        intervals[j] = None
                        flag = True
                        a[0] = min(a[0], b[0])
                        a[1] = max(a[1], b[1])
        result = []
        for a in intervals:
            if a is not None:
                result.append(a)
        return result


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(s.merge([[1, 4], [4, 5]]) == [[1, 5]])
