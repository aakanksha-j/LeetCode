"""1035. Uncrossed Lines
Medium
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
 

Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000"""

# top down recursive dp

# without lru cache, time limit exceeded

from functools import lru_cache
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # top down recursive dp
        # time O(m.n)
        # space O(m.n)
        # similar to lcs - https://leetcode.com/problems/longest-common-subsequence/discuss/3432885/python3-top-down-bottom-up-space-optimized
        m, n = len(nums1), len(nums2)
        @lru_cache(None)
        def dfs(i,j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dfs(i-1, j-1)
            else:
                return max(dfs(i, j-1), dfs(i-1, j))
            
        return dfs(m-1, n-1)

# 2d bottom up iterative dp

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # time O(m.n)
        # space O(m.n)
        # similar to lcs - https://leetcode.com/problems/longest-common-subsequence/discuss/3432885/python3-top-down-bottom-up-space-optimized
        m, n = len(nums1), len(nums2)
        dp = [[0]* (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]
    
# Space optimized bottom up iterative dp

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # time O(m.n)
        # space O(n)
        # similar to lcs - https://leetcode.com/problems/uncrossed-lines/discuss/3510548/Image-Explanation-Recursion-greater-Memo-greater-DP-greater-DP-Optimized-C%2B%2BJavaPython
        m, n = len(nums1), len(nums2)
        dp = [0]* (n+1)
        for i in range(1, m+1):
            pre = dp[:]
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = 1 + pre[j-1]
                else:
                    dp[j] = max(dp[j-1], pre[j])
        return dp[-1]