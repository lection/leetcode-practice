"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

=====================================
直接上回溯比较简单 但是应该要超时 这是一个 n^n 解
加入一个针对nums的缓存 但是依然超时
"""


class Solution:
    def maxCoins(self, nums) -> int:
        if not nums:
            return 0

        cache = {}

        def rec(ns):
            if not ns:
                return 0

            key = str(ns)
            if key in cache:
                return cache[key]

            length = len(ns)
            r = 0
            for i in range(length):
                n = ns[i]
                if i > 0:
                    n *= ns[i-1]
                if i < (length - 1):
                    n *= ns[i+1]

                r = max(r, n + rec(ns[:i]+ns[i+1:]))

            cache[key] = r
            return r

        return rec(nums)


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
