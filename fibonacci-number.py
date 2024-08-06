class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def fibonacci(num):
            if num not in memo:
                memo[num] = fibonacci(num - 1) + fibonacci(num - 2)

            return memo[num]

        return fibonacci(n)
