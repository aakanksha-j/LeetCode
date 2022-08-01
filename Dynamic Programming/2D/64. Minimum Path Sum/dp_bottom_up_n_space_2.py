class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # O(cols) space dp bottom up iterative solution

        # similar to unique paths 2 O(n) solution
        # https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).

        # time: O(m.n) for traversing the entire matrix
        # space: O(n) - extra space for above row like paint house pre = dp[:]

        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]

        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            pre = dp[:]
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j - 1], pre[j])

        return dp[-1]

        
