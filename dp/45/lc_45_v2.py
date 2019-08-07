"""
参考网友思路
现在陷入了看什么都直接套DP的思路，有点儿僵化。
其实可以直接遍历数组，记录下每一跳的最大值即可。
在最大值范围内寻找下一跳的最大值
还是先从O(n)的方式尝试考虑
====================通过了 接下来就是优化环节了
"""


class Solution:
    def jump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return 0

        steps = 0
        step_max = 0
        _max = 0

        last_index = len(nums) - 1

        for i in range(len(nums)):
            _max = max(i+nums[i], _max)
            if _max >= last_index:
                return steps + 1

            if i == step_max:
                step_max = _max
                steps += 1


s = Solution()
print(s.jump([2, 3, 1, 1, 4]) == 2)
print(s.jump([2, 3, 0, 1, 4]) == 2)
print(s.jump([0]) == 0)
