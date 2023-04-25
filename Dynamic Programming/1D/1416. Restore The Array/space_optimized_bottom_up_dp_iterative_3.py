class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # space optimized bottom up dp iterative 
        
        # time O(n * logk) for loop inside for loop run for k times
        # space O(logk) for dp array of size logk+1 i.e m+1
        
        n = len(s)
        m = len(str(k))
        dp = [1] + [0]*m
        
        for i in range(n):
            if s[i] == '0':
                dp[i % (m+1)] = 0
                continue
        
            for j in range(i, min(n, i+m)):
                if int(s[i: j+1]) > k:
                    break
                dp[(j+1) % (m+1)] += dp[i % (m+1)] % int(1e9 + 7)
                
            dp[i % (m+1)] = 0
                
        return dp[n % (m+1)] % int(1e9 + 7)
    
# https://leetcode.com/problems/restore-the-array/solution/

