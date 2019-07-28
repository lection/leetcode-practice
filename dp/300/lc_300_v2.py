"""
严格来说 2出现的时候5就可以去掉了 3出现的时候10可以失效了
同一个计数在从前到后的遍历过程中 只有一个 保留最小的
删除和查找都用二分查找的方式
基本实现n*log(n) 速度从 1000ms 优化到 68ms 打败85.71%
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        bs_data = [nums[0]]
        count_cache = {1: nums[0]}
        num_cache = {nums[0]: 1}

        def bs(t):
            low = 0
            high = len(bs_data) - 1
            while low <= high:
                mid = low + (high - low) // 2
                v = bs_data[mid]
                if v == t:
                    return mid
                if v < t:
                    low = mid + 1
                else:
                    high = mid - 1

            return low - 1

        def fn(t, index, count):
            bs_data.insert(index + 1, t)
            if count in count_cache:
                v = count_cache[count]
                bs_data.remove(v)
                num_cache.pop(v)
            count_cache[count] = t
            num_cache[t] = count

        for i in range(1, len(nums)):
            t = nums[i]
            if t in num_cache:
                continue
            index = bs(t)
            if index < 0:
                fn(t, index, 1)
                continue

            fn(t, index, num_cache[bs_data[index]] + 1)

        return max(num_cache.values())


s = Solution()
# print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# print(s.lengthOfLIS([2, 2]))
print(s.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
