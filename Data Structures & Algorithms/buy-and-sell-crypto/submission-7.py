class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        minVal = prices[0]
        
        for sell in prices:
            maxProfit = max(maxProfit, sell-minVal)
            minVal = min(sell, minVal)
        
        return maxProfit