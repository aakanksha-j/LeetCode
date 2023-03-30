# iterative dp solution
# O(N^4)
# https://leetcode.com/problems/scramble-string/discuss/29396/Simple-iterative-DP-Java-solution-with-explanation

# Let F(i, j, k) = whether the substring S1[i..i + k - 1] is a scramble of S2[j..j + k - 1] or not
# 		 * Since each of these substrings is a potential node in the tree, we need to check for all possible cuts.
# 		 * Let q be the length of a cut (hence, q < k), then we are in the following situation:
# 		 * 
# 		 * S1 [   x1    |         x2         ]
# 		 *    i         i + q                i + k - 1
# 		 * 
# 		 * here we have two possibilities:
# 		 *      
# 		 * S2 [   y1    |         y2         ]
# 		 *    j         j + q                j + k - 1
# 		 *    
# 		 * or 
# 		 * 
# 		 * S2 [       y1        |     y2     ]
# 		 *    j                 j + k - q    j + k - 1
# 		 * 
# 		 * which in terms of F means:
# 		 * 
# 		 * F(i, j, k) = for some 1 <= q < k we have:
# 		 *  (F(i, j, q) AND F(i + q, j + q, k - q)) OR (F(i, j + k - q, q) AND F(i + q, j, k - q))
# 		 *  
# 		 * Base case is k = 1, where we simply need to check for S1[i] and S2[j] to be equal 
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
      
        for k in range(2, n+1):
            for i in range(n+1-k):
                for j in range(n+1-k):
                    for q in range(1, k):
                        
                        dp[k][i][j] |= dp[q][i][j] and dp[k-q][i+q][j+q] or \
                                      dp[q][i][j+k-q] and dp[k-q][i+q][j]
                        
        return dp[n][0][0]
    
# https://leetcode.com/problems/scramble-string/discuss/3357574/day-364-100-java-c-python-explained-intution-dry-run-proof
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
      
        for k in range(2, n+1):
            for i in range(n+1-k):
                for j in range(n+1-k):
                    for q in range(1, k):
                        dp1 = dp[q][i]
                        dp2 = dp[k-q][i+q]
                        dp[k][i][j] |= dp1[j] and dp2[j+q]
                        dp[k][i][j] |= dp1[j+k-q] and dp2[j]
                        
        return dp[n][0][0]