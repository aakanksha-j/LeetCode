from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # neetcode solution
        # return the fewest number of coins to make up that amount.
        # using bottom-up approach and dp 
        
        # in dp array, we will store the minimum number of coins we will need for that particular amount
        # since bottom up approach is used, we will build dp array from 0 to amount, using the coins array which provides the denominations available.
        # use 2 for loops, one to reach amount and inner one to choose coin denomination
        # time: O(amount*coin denomination) - 2 for loops
        # space: O(amount) - dp array - memoization table
        
        dp = [(amount + 1)] * (amount + 1)
        dp[0] = 0 # base case for 0 amount
        
        for i in range(1, (amount + 1)): # base case 0 already defined, so start from 1
            for coin in coins:
                if i - coin >= 0:
                    # recurrence relation
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # edge case: no solution exists, amount cannot be formed by any of the given denominations. eg. amount 3 coin = [2]
        print(dp)
        return dp[amount] if dp[amount] != (amount + 1) else -1 
        
        
        
# leetcode solution - bottom up dp iterative 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # similar to combination sum 4, dice throw, coin change 2
        
        # time O(amount + 1 * coins)
        # space O(amount + 1) for dp array
        
        dp = [0] + [amount + 1] * (amount)
        for coin in coins:
            for amount_sum in range(coin, amount + 1):
                dp[amount_sum] = min(dp[amount_sum], 1 + dp[amount_sum - coin])
                #print(dp)
        return dp[amount] if dp[amount] != (amount + 1) else -1