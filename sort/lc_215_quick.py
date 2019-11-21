"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
================
用快速排序的思路做选择 时间复杂度 O(n)
这个比直接用最小堆更难想到
速度很慢，什么鬼
"""

class Solution:
    def findKthLargest(self, nums, k) -> int:
        if not nums or len(nums) < k:
            return None

        def partition(li, ri):
            if li >= ri:
                return li
            pivot = nums[ri]
            idx = left
            for i in range(li, ri):
                if nums[i] < pivot:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    idx += 1
            nums[ri], nums[idx] = nums[idx], nums[ri]
            return idx

        left = 0
        right = len(nums) - 1
        # 第k大，就是第 length - k + 1 小
        k = len(nums) - k
        # 用while写更准确 但是总有怕死循环的担心 这么写更安全
        for _ in range(len(nums)):
            pivot_idx = partition(left, right)
            if pivot_idx == k:
                return nums[pivot_idx]
            elif pivot_idx < k:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5)
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4)
