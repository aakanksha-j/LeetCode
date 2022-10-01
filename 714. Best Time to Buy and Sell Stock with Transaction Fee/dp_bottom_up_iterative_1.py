class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # leetcode solution
        
        # time: O(N)
        # space: O(1)
        
        # set starting value
        sell_not_hold = 0
        buy_hold = -prices[0]
        
        # transition equation
        for i in range(1, len(prices)):
            sell_not_hold = max(sell_not_hold, buy_hold + prices[i] - fee)
            buy_hold = max(buy_hold, sell_not_hold -prices[i])
            
        return sell_not_hold # last value