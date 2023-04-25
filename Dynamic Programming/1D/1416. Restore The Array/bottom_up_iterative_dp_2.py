class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # bottom up dp iterative 
        
        # time O(n * logk) for loop inside for loop run for k times
        # space O(n) for dp array
        
        dp = [1] + [0]*len(s)
        
        for i in range(len(s)):
            if s[i] == '0':
                continue
            
            for j in range(i, min(len(s), i+len(str(k)))):
                if int(s[i: j+1]) > k:
                    break
                dp[j+1] += dp[i] % (10**9 + 7)
                
        return dp[-1] % int(1e9 + 7)
    
# https://leetcode.com/problems/restore-the-array/solution/