class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1

        for step in range(2, n + 1):
            memo[step] = memo[step - 1] + memo[step - 2]

        return memo[n]