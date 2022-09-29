class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # similar to kadane algorithm
        
        # time: O(N)
        # space: O(1)
                
        buy_hold = -prices[0]
        sell_not_hold = 0
        
        for price in prices[1:]:
            sell_not_hold, buy_hold,  = max(sell_not_hold, buy_hold + price), max(buy_hold, sell_not_hold - price) 
        return sell_not_hold