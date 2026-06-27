class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_start = best_end = 0

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = (
                    s[start] == s[end] and
                    (length == 2 or dp[start + 1][end - 1])
                )

                if dp[start][end]:
                    best_start, best_end = start, end

        return s[best_start:best_end + 1]