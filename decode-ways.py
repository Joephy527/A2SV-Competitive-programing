class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        memo = [0] * (n + 1)
        memo[0], memo[1] = 1, 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            if one_digit != 0:
                memo[i] += memo[i - 1]

            if 10 <= two_digits <= 26:
                memo[i] += memo[i - 2]

        return memo[n]
