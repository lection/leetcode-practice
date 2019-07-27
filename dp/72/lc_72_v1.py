class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        if l1 == 0 or l2 == 0:
            return max(l1, l2)

        dp = [[0] * l2 for _ in range(l1)]

        def fn(i, j):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            return dp[i][j]

        for i in range(l1):
            for j in range(l2):
                dp[i][j] = 1 + min(
                    fn(i-1, j),
                    fn(i, j-1),
                    fn(i-1, j-1) - (1 if word1[i] == word2[j] else 0)
                )

        return dp[-1][-1]


s = Solution()
print(s.minDistance('horse', 'ros') == 3)
print(s.minDistance('intention', 'execution') == 5)
