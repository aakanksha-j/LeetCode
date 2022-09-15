class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane algorithm from maximum subarray learnt from neeetcode
        minprice = prices[0]
        maxdiff = 0
        for n in prices:
            if n > minprice:
                maxdiff = max(n-minprice, maxdiff)
            else:
                minprice = n
        return maxdiff


        
