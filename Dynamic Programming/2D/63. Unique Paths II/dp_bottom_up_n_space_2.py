class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # O(cols) space dp bottom up iterative solution
        # https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).

        # time: O(m.n) - iterate every element in matrix
        # space: O(n) - store only the elements in above row

        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0 for j in range(n)]
        dp[0] = 1

        for j in range(1, n):
            dp[j] = (dp[j - 1] + dp[j]) * (1 - obstacleGrid[0][j])

        for i in range(1, m):
            dp[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, n):
                dp[j] = (dp[j - 1] + dp[j]) * (1 - obstacleGrid[i][j])

        return dp[-1]
