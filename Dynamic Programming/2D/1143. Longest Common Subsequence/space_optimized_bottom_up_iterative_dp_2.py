class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # space optimized bottom up iterative dp
        m, n = len(text1), len(text2)
        dp = [0] * (n+1) # remember n not m, will generate index out of list error otherwise
        for i in range(1, m+1):
            pre = dp[:]
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[j] = pre[j-1] + 1
                else:
                    dp[j] = max(dp[j-1], pre[j])
            

        return dp[n] # or dp[-1] 
    

# time O(m.n) m,n = len(text1), len(text2)
# space O(n) 
    
# input:
# "abcde"
# "acdefg"
# print(dp, pre)
# [0, 1, 1, 1, 1, 1, 1] [0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1] [0, 1, 1, 1, 1, 1, 1]
# [0, 1, 2, 2, 2, 2, 2] [0, 1, 1, 1, 1, 1, 1]
# [0, 1, 2, 3, 3, 3, 3] [0, 1, 2, 2, 2, 2, 2]
# [0, 1, 2, 3, 4, 4, 4] [0, 1, 2, 3, 3, 3, 3]

# https://leetcode.com/problems/longest-common-subsequence/discuss/1473350/Python-Bottom-up-DP-From-O(M*N)-to-O(N)-Space-Clean-and-Concise