"""
传统DP 可惜只打败了5%
"""


class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        if not prices:
            return 0

        cache = (0, -fee, 0)
        for idx in range(1, len(prices)):
            diff = prices[idx] - prices[idx-1]
            cache = (
                max(cache[0], cache[2]),
                max(diff+cache[1], cache[0]-fee, cache[2]-fee),
                diff + cache[1]
            )

        return max(cache)


s = Solution()
print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
