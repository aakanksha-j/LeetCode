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



# space optimized approach - Bottom up iterative dp solution in Python3
# Inspired from https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355940/C%2B%2B-Coin-Change-2 space optimized approach similar to Coin Change 2.

# time O((dice + 1)(target + 1)(face+1))
# space O(target)

# Important to make current array 0 because we want to make starting values 0
# eg. dice 3 faces 3 target 4
# 10000
# 01110
# 00123
# 00013

def numRollsToTarget(self, n: int, k: int, target: int) -> int:
	mod = 10**9 + 7
                
	dp = [1] + [0]*target   # dp[0] must be 1 because we can reach target 0 in 1 way, array size - target + 1

	for dice in range(1, n + 1):  # run dice from 1 to n
		pre = dp[:] # use to store copy of previous array
		dp = [0]*(target + 1) # make current array 0 to avoid previous feedback 
		for face in range(1, k + 1):  # face loop before target, to get combinations (121 is same as 211)                     
			for target_sum in range(face, target + 1): # run from face to avoid target_sum - face becoming negative
				dp[target_sum] += pre[target_sum - face] 

	return dp[target] % mod

# helpful youtube video link - https://www.youtube.com/watch?v=UiYVToWORMY&t=617s&ab_channel=alGOds