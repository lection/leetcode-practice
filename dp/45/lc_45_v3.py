"""
练练回溯
======================
看看回溯剪枝能否通过
======================
并不能 其实并没有剪掉什么 失败
"""


class Solution:
    def jump(self, nums) -> int:
        if not nums:
            return 0

        length = len(nums)
        last_idx = length - 1
        cache = [None] * length

        def rec(idx):
            if idx >= last_idx:
                return 0

            if cache[idx] is not None:
                return cache[idx]

            r = length

            for i in range(1, nums[idx] + 1):
                r = min(r, rec(idx + i))

            r += 1
            cache[idx] = r
            return r

        return rec(0)


s = Solution()
print(s.jump([2, 3, 1, 1, 4]) == 2)
print(s.jump([2, 3, 0, 1, 4]) == 2)
print(s.jump([0]) == 0)
print(s.jump([1, 1, 1, 1]) == 3)
