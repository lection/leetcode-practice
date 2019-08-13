"""
换一个思路来实现，并且参考网上做法，使用python的缓存库和语法糖
从最后一个戳破的气球角度来考虑，十分容易的对数据进行分组和缓存，时间复杂度虽然依然是n^n
如果idx是最后一个戳破的气球，则0-idx idx-end两个分组的最优解无论怎么算，都不会突破idx这个下标 所以可以直接做为子问题去解决
================
虽然本质上和V1版本不同，但是缓存速度不一样，V1的缓存还是要遍历现有数组做缓存，效率低下
"""
from functools import lru_cache


class Solution:
    def maxCoins(self, nums) -> int:
        if not nums:
            return 0

        nums = [1] + nums + [1]

        @lru_cache(None)
        def rec(left, right):
            r = 0
            for i in range(left, right):
                lv = nums[left - 1]
                rv = nums[right]
                r = max(
                    r,
                    nums[i] * lv * rv +
                    rec(left, i) + rec(i + 1, right)
                )

            return r

        return rec(1, len(nums) - 1)


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
