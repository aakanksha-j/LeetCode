def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 0/1 knapsack, either take or don't take current item
        # space optimized bottom up dp
        
        # time O(k * i * j) group length * n * minProfit
        # and space O(i*j) n * minProfit
        
        mod = 10**9 + 7
        dp = [[0] * (minProfit + 1) for i in range(n + 1)] 
        
        dp[0][0] = 1 # moving on all k crimes, 
        
        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            for i in range(n, g - 1, -1): # removed i - g >= 0 condition
                for j in range(minProfit, -1, -1):
                        # removed not_include condition
                        dp[i][j] += dp[i - g][max(j - p, 0)] # 0 because array starts from 0

        output = 0
        for i in range(n + 1):
            output += dp[i][minProfit]
        
        return output % mod # error if mod not divided