class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # O(n) space optimized bottom up dp 
        n = len(s)
        dp, dpPrev = [0] * n, [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j - 1] + 2
                else:
                    dp[j] = max(dpPrev[j], dp[j - 1])
            dp, dpPrev = dpPrev, dp

        return dpPrev[n - 1]