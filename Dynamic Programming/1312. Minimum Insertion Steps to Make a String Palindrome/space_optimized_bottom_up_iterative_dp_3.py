class Solution:
    def minInsertions(self, s: str) -> int:
        # space optimized bottom up dp
        
        # time O(n^2)
        # space O(n)
        
        N = len(s)
        dp = [0] * (N + 1) 
        
        for start in reversed(range(N)):
            prev = 0
            for end in range(start, N):
                # print(start, end)
                tmp = dp[end]
                # print('tmp', tmp)
                if s[start] == s[end]:
                    dp[end] = prev
                else:
                    dp[end] = 1 + min(dp[end], dp[end - 1])
                prev = tmp
                # print('prev', prev)
            
        return dp[N - 1]