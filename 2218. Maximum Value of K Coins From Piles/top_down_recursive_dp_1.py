"""2218. Maximum Value of K Coins From Piles
Hard
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

Example 1:


Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
 

Constraints:

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 105
1 <= k <= sum(piles[i].length) <= 2000
"""
import functools
from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/discuss/1887010/JavaC%2B%2BPython-Top-down-DP-solution
        # https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/discuss/3417959/Image-Explanation-Top-Down-DP-Easy-and-Concise-C%2B%2BJavaPython

        @functools.lru_cache(None)
        def dp(rem_k, i):
            if rem_k == 0 or i == len(piles): return 0
            
            maximum = dp(rem_k, i + 1) # skip cur pile
            
            current = 0
            for j in range(min(len(piles[i]), rem_k)): # grab 1..rest_k coins from cur pile
                current += piles[i][j]
                maximum = max(current + dp(rem_k - (j + 1), i + 1), maximum)
            
            return maximum
            
        return dp(k, 0) 
    
# time: O(m * n * k)
# space: O(n * k)
# where n = len(piles), m = sum(len(piles[i])

# not using cache but 2d dp array
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # https://www.youtube.com/watch?v=ZRdEd_eun8g&ab_channel=NeetCodeIO
        
        n = len(piles)
        dp = [[-1]* (k + 1) for _ in range(n)]
        
        def dfs(rem_k, i):
            if rem_k == 0 or i == n: return 0
            
            if dp[i][rem_k] != -1:
                return dp[i][rem_k]
            
            dp[i][rem_k] = dfs(rem_k, i + 1) # skip cur pile
            
            current = 0
            for j in range(min(len(piles[i]), rem_k)): # grab 1..rest_k coins from cur pile
                current += piles[i][j]
                dp[i][rem_k] = max(current + dfs(rem_k - (j + 1), i + 1), dp[i][rem_k])
            
            return dp[i][rem_k]
            
        return dfs(k, 0) 