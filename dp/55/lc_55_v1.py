"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

==============================================
直接参考45题的最优解法似乎就可以
迭代过程中始终关注当前最大值 当最大值大于长度即成功
如果当前迭代位置大于当前最大值则失败
"""


class Solution:
    def canJump(self, nums) -> bool:
        if not nums:
            return False

        _max = 0
        length = len(nums)
        last_idx = length - 1

        for i in range(length):
            if i > _max:
                return False

            _max = max(_max, i + nums[i])

            if _max >= last_idx:
                return True


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
