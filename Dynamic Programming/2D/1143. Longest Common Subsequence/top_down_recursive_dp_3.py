from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top down recursive dp
        
        m, n = len(text1), len(text2)
        
        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0: # reached end
                return 0
            if text1[i] == text2[j]: # i and j not i-1, j-1
                return dfs(i-1, j-1) + 1
            else:
                return max(dfs(i, j-1), dfs(i-1, j))
            
        return dfs(m-1, n-1)
    
# "bsbininm"
# "jmjkbkjkv"

# https://leetcode.com/problems/longest-common-subsequence/discuss/350993/Python-dp-and-recursive