class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # own approach - dp bottom up solution

        # time: O(m.n) - iterate every element in matrix
        # space: O(m.n) - store matrix dp of size m.n

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    if i == 0 and j == 0 and obstacleGrid[i][j] == 0:
                        dp[i][j] = 1
                    elif i == 0 and dp[i][j - 1] == 0:
                        dp[i][j] = 0
                    elif j == 0 and dp[i - 1][j] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
