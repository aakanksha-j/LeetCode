class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # time O(dice + 1 * target + 1 * faces)
        # space O(dice + 1 * target + 1)
        
        # https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/686109/Java-DP-Explanation-with-diagram       
        
        if n * k < target: return 0
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        mod = 10**9 + 7
        dp[0][0] = 1
        for dice in range(1, n + 1): 
            for target_sum in range(1, target + 1):
                for face in range(1, k + 1):
                    if target_sum - face < 0: continue
                    dp[dice][target_sum] += dp[dice - 1][target_sum - face]
                    # dp[dice][target] = sum(dp[dice - 1][target - 1] + dp[dice - 1][target - 2] + ... dp[dice - 1][target - faces]
                
        return dp[n][target] % mod



# space optimized - to do
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355940/C%2B%2B-Coin-Change-2

