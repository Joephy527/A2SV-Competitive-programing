class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_till_now = min_till_now = prices[0]
        profit = 0

        for price in prices:
            if price < max_till_now:
                profit += max_till_now - min_till_now
                min_till_now = max_till_now = price
            else:
                max_till_now = price

        profit += max_till_now - min_till_now

        return profit