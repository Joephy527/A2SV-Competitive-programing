class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        comp = 0
        for i in range(1, len(prices)):
            if prices[p] >= prices[i]:
                p = i
            else:
                new_comp = prices[i] - prices[p]
                if new_comp > comp:
                    comp = new_comp

        return comp
