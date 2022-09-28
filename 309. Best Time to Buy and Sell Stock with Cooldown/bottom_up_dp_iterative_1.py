class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # own approach using neetcode solution and similar to best time to buy and sell stock IV

        # time: O(N) - iterate over every element in array
        # space: O(N) - for dp array

        n = len(prices)
        
        # special case
        if n <= 1:
            return 0
        
        # dp[i][k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[-math.inf] * 2 for _ in range(n)]
        
        # set starting value
        dp[-1][0] = 0 # important, missed entering this and got wrong answer for [2,1,4]
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        
        # fill the array
        for i in range(1, n):
            #print(dp)
            # transition equation
            #print(dp[i-1][0], dp[i-1][1])
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) 
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            #print(dp)
            
        res = max(dp[i][0] for i in range(n))
        return res
        
        