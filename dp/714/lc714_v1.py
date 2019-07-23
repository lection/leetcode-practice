"""
递归+cache
尝试从终点向下递归
状态 0不操作 1买入操作 2卖出操作
"""


def maxProfit(prices, fee: int) -> int:
    if not prices:
        return 0

    def rec(idx):
        if idx == 0:
            return [0, -fee, 0]
        diff = prices[idx] - prices[idx - 1]
        prev = rec(idx - 1)
        return (
            max(prev[0], prev[2]),
            max(diff + prev[1], prev[0] - fee, prev[2] - fee),
            diff + prev[1],
        )

    return max(rec(len(prices) - 1))


print(maxProfit([1, 3, 2, 8, 4, 9], 2))
