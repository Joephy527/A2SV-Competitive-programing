class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * (max(costs) + 1)
        max_bars = 0

        for cost in costs:
            count[cost] += 1

        for coin in range(1, len(count)):
            while count[coin] and coin <= coins:
                max_bars += 1
                count[coin] -= 1
                coins -= coin

        return max_bars