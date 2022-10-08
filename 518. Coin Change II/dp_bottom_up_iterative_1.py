class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom up dp iterative solution
        
        # O(coins * amount) time
        # O(amount) space
                
        dp = [1] + [0]*amount
        
        for coin in coins:
            for amount_sum in range(coin, amount + 1):
                dp[amount_sum] += dp[amount_sum - coin] 
        return dp[-1]
    

# we have to calculate combinations (121 is equal to 211) and not permutations
# therefore start first for loop with coins so that smaller coin is not repeated 
# then run amount_sum from coin to target
# similar to combination sum 4, dice throw, coin change