class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def dp(num):
            if num == 0: return 0
        
            if num == 1 or num == 2: return 1

            if num not in memo:
                memo[num] = dp(num - 1) + dp(num - 2) + dp(num - 3)

            return memo[num]

        return dp(n)
