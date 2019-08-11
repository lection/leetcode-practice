"""
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
=========================
额，似乎这个题跟DP没啥关系额。
我直接用最多的任务数乘n就可以解决大部分问题了。

情况1 最多任务-1 * n 大于总任务数 - 最多任务数 就这个数就行了
情况2 最多任务-1 * n 小于总任务数 - 最多任务数 总任务数就行了
"""
A_0 = ord('A')


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        if not tasks:
            return 0
        if n <= 0:
            return len(tasks)

        counts = [0] * 26
        for t in tasks:
            idx = ord(t) % A_0
            counts[idx] += 1

        _max = 0
        _max_count = 0

        for count in counts:
            if count > _max:
                _max = count
                _max_count = 1
            elif count == _max:
                _max_count += 1

        return max(len(tasks), (_max - 1) * (n + 1) + _max_count)


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
