class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # own approach - dp bottom up solution

        # time: O(m.n) - iterate every element in matrix
        # space: O(m.n) - store matrix dp of size m.n

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
