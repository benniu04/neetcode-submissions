class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        minPrice = prices[0]
        for right in prices:
            if right < minPrice:
                minPrice = right
            else:
                profit = max(profit, right - minPrice)
        return profit

