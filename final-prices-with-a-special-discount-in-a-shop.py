class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]

        for i in range(len(prices) - 1, -1, -1):
            while stack[-1] > prices[i]:
                stack.pop()

            stack.append(prices[i])
            prices[i] -= stack[-2]

        return prices
