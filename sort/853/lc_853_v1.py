"""
N  辆车沿着一条车道驶向位于 target 英里之外的共同目的地。

每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。

一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。

此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。

车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。

即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。

 

会有多少车队到达目的地?

 

示例：

输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
输出：3
解释：
从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。

提示：

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
所有车的初始位置各不相同。
====================
计算每辆车到达终点的时间 按position排序 连续递增的一组就可以合并为一个车队
先用zip + sort实现 比较方便快捷 但是空间占用的比较大
====================
我想错了 只看递增是不行的 如果倒序 查看有几个更高的点 应该是可以的
假如最终消耗时间是 4 2 6  3 5 1 2，倒序看几个递增的高点 分别是 2 5 6
三个高点会把他们后方速度更快的所有点都合并成一个车队
====================
轻松通过 内存占用略高 可以用手动快速排序优化一下 不折腾了
"""


class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        if not position:
            return 0
        result = 0
        last_max = 0
        for d in sorted(zip(position, speed), reverse=True):
            t = (target - d[0]) / d[1]
            if t > last_max:
                result += 1
                last_max = t
        return result


s = Solution()
print(s.carFleet(10, [2, 4], [3, 2]) == 1)
print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3)
print(s.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1)
