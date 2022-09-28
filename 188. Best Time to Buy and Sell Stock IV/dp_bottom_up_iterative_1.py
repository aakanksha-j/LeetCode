class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # leetcode solution - dp
        # time: O(nk) if 2k <= n, O(n)if 2k > n, since we have 2 for loops
        # space: O(nk)
        n = len(prices)
        if n == 0 or k == 0: return 0
        
        # edge case:
        if 2*k > n:
            output = 0
            for i, j in zip(prices[1:], prices[:-1]):
                output += max(i - j, 0)
            return output
        
        # dp[i][used_k][ishold] = balance
        # ishold: 0 - notholding, 1 - holding
        dp = [[[-math.inf]*2 for _ in range(k + 1)] for _ in range(n)]
        
        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        
        # fill the array
        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j][0] = max(dp[i - 1][j][1] + prices[i],dp[i - 1][j][0]) # selling + not holding
                if j > 0:
                    dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i],dp[i - 1][j][1]) # buying + holding
                
        #print(dp)
        output = max(dp[n - 1][j][0] for j in range(k + 1))
        return output
        
        