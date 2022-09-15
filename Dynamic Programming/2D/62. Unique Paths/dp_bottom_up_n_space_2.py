class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(n) space - dp bottom up iterative solution

        # O(m.n) time but O(n) space
        # https://leetcode.com/problems/unique-paths/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).
        # paint house also done in O(n) space using similar solution

        dp = [1 for _ in range(n)] # or [1]*n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]
