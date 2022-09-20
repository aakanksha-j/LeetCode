    

# similar to paint house, unique paths sums
# here, array size of dp is n+1 instead of n 
# we run both for loops from 1 to m+1 and 1 to n+1, first element is 0 as we needed to initialize

# 1. 2D DP solution 
# time O(M.N) - two for loops
# space O(M.N) - array in array dp[i][j] 

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        m, n = len(A), len(B)
        
        ans = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):           
            for j in range(1, n + 1):
                #print(i, j, dp)
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else: 
                    dp[i][j] = 0
                
        return max(max(value) for value in dp)
        




# 2. space optimized 2D to 1D dp 
# time: O(M.N) - iterate every element in matrix
# space: O(min(M,N)) store prev state of dp in pre variable

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        m, n = len(A), len(B)
        
        ans = 0
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):            
            pre = dp[:]            
            for j in range(1, n + 1):
                #print(i, j, dp)
                if A[i - 1] == B[j - 1]:
                    dp[j] = pre[j - 1] + 1
                else: 
                    dp[j] = 0
            ans = max(ans, max(dp))
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        