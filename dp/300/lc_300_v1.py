class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        def dfs(curr, idx):
            if idx >= len(nums):
                return len(curr)
            v = nums[idx]
            idx += 1
            if curr and curr[-1] >= v:
                return dfs(curr, idx)
            return max(dfs(curr + [v], idx), dfs(curr, idx))

        return dfs([], 0)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
