class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            right += 1
        
        return maxProfit
            
