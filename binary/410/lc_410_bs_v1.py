"""
思路很暴力
nums中的最大值，是解的下限，sum(nums)是解的上限。
已知上限和下限，就可以使用二分查找进行校验。

校验手段符合贪心条件，迭代nums并贪心的累加子数组的和，直至和>最大值，查看最终子数组的数量是否符合条件。

n的范围有限 故时间复杂度 log(n) * n
"""


class Solution:
    def splitArray(self, nums, m: int) -> int:
        if not nums:
            return 0

        def check(mv):
            count = 1
            sum_value = 0
            for n in nums:
                sum_value += n
                if sum_value > mv:
                    count += 1
                    sum_value = n
                    if count > m:
                        return False

            return True

        hi = sum(nums)
        low = max(nums)
        while low <= hi:
            mid = low + (hi - low) // 2
            if check(mid):
                hi = mid - 1
            else:
                low = mid + 1

        return low


s = Solution()
print(s.splitArray([7, 2, 5, 10, 8], 2))
