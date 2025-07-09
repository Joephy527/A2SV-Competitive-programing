class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = p = 0

        for s in range(len(prices)):
            if prices[p] > prices[s]:
                p = s

            max_profit = max(max_profit, prices[s] - prices[p])

        return max_profit