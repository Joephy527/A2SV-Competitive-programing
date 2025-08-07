class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    memo[amt] = min(
                        memo[amt],
                        memo[amt - coin] + 1
                    )

        return memo[amount] if memo[amount] != float("inf") else -1