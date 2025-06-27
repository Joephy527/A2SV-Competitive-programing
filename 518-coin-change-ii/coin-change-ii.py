class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0] * (amount + 1)
        memo[0] = 1

        for coin in coins:
            for amt in range(coin, amount + 1):
                memo[amt] += memo[amt - coin]
        
        return memo[-1]