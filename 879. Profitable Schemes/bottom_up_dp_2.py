def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 0/1 knapsack, either take or don't take current item
        # bottom up dp
        
        # time and space O(k*i*j) profit.length*noofmembers*minProfit
        
        mod = 10**9 + 7
        dp = [[[0] * (minProfit + 1) for i in range(n + 1)] for k in range(len(group) + 1)]
        
        dp[0][0][0] = 1 # moving on all k crimes, 
        
        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            for i in range(n + 1):
                for j in range(minProfit + 1):
                    dp[k][i][j] += dp[k - 1][i][j]
                    if i - g >= 0: # equivalent to i + group[k] <= n
                        dp[k][i][j] += dp[k - 1][i - g][max(j - p, 0)] % mod # 0 because array starts from 0

        output = 0
        for i in range(n + 1):
            output += dp[len(group)][i][minProfit]
        
        return output % mod # remember to divide by mod here even if divided earlier else value is too large