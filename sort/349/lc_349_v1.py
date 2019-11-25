"""
计算两个数组交集
思路也简单
1 归并排序的套路 O(n * log(n))
2 哈希 直接set交集 O(n)

哈希太简单 一行就行 list(set(nums1) & set(nums2))
"""


class Solution:
    def intersection(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        li = ri = 0
        while li < len(nums1) and ri < len(nums2):
            if nums1[li] == nums2[ri]:
                if not result or nums1[li] != result[-1]:
                    result.append(nums1[li])
                li += 1
                ri += 1
            elif nums1[li] > nums2[ri]:
                ri += 1
            else:
                li += 1
        return result


s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]) == [2])
print(sorted(s.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == sorted([9, 4]))
