"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

==============
乍一看没啥难度 跟56的排序算法没啥区别
轻松通过 内存消耗有点儿浪费 接下来v2弄个原地操作的
"""


class Solution:
    def insert(self, intervals, newInterval):
        result = []
        last = newInterval
        flag = True
        for a in intervals:
            if a[1] < last[0]:
                result.append(a)
            elif a[0] > last[1]:
                if flag:
                    flag = False
                    result.append(last)
                result.append(a)
            else:
                last[0] = min(last[0], a[0])
                last[1] = max(last[1], a[1])
        if flag:
            result.append(last)
        return result


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
