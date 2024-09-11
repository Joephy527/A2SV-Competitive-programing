class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0
        
        for money in range(1, amount + 1):
            for coin in coins:
                if money - coin >= 0:
                    memo[money] = min(memo[money], 1 + memo[money - coin])
                
        return memo[amount] if memo[amount] != float("inf") else -1
