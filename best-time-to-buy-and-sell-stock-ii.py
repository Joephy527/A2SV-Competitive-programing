class Solution(object):
    def maxProfit(self, prices):
        profit = 0

        for i in range(len(prices)-1):
            curPrice = prices[i+1] - prices[i]
            profit += curPrice if curPrice > 0 else 0
        
        return profit
