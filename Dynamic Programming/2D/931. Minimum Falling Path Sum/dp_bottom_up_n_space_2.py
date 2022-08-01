class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # O(cols) space dp bottom up iterative solution

        # inspired from paint house sum

        # time: O(m.n) - iterate every element in matrix
        # space: O(n) - store only the elements in above row

        m = len(matrix)
        n = len(matrix[0])

        dp = matrix[0]

        for i in range(1, m):
            #print(dp)
            pre = dp[:]
            for j in range(n):
                if j == 0:
                    dp[j] = matrix[i][j] + min(pre[:(j + 2)])
                elif j == (n - 1):
                    dp[j] = matrix[i][j] + min(pre[(j - 1):])
                else:
                    dp[j] = matrix[i][j] + min(pre[(j - 1): (j + 2)])

        #print(dp)
        return min(dp)
