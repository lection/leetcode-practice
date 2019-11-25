"""
琢磨琢磨 一次遍历怎么实现
暂时的想法 可以两个下标指针 一个从0开始 一个从末尾开始
遇到0移动下标 遇到2移动末尾
===========
额，各种细节逼疯我 总算过了
"""


class Solution:
    def sortColors(self, nums):
        i0 = 0
        i2 = len(nums) - 1
        i = 0
        while i <= i2:
            n = nums[i]
            if n == 0:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1
                i += 1
            elif n == 2:
                nums[i], nums[i2] = nums[i2], nums[i]
                i2 -= 1
            else:
                i += 1


s = Solution()
# d = [2, 0, 2, 1, 1, 0]
d = [2, 0, 1]
# d = [1, 2, 0]
s.sortColors(d)
print(d)
