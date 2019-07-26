class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if record[i][j] != -1:
                return record[i][j]
            if word1[i] == word2[j]:
                record[i][j] = helper(i - 1, j - 1)
                return record[i][j]
            record[i][j] = 1 + min(helper(i, j - 1), helper(i - 1, j), helper(i - 1, j - 1))
            return record[i][j]

        length1 = len(word1) - 1
        length2 = len(word2) - 1
        record = [[-1] * (length2 + 1) for i in range(length1 + 1)]
        return helper(length1, length2)


s = Solution()
print(s.minDistance('horse', 'ros') == 3)
print(s.minDistance('intention', 'execution') == 5)
