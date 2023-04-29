class Solution:
    def minInsertions(self, s: str) -> int:
        
        N = len(s)
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        for start in reversed(range(N)):
            for end in range(start, N):
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1]
                else:
                    dp[start][end] = 1 + min(dp[start + 1][end], dp[start][end - 1])
            
        return dp[0][N - 1]
    
# time O(n^2)
# space O(n^2)