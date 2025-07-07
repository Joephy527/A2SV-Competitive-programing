class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        max_left = max_right = 0

        for end in range(n):
            for start in range(end + 1):
                if (
                    s[start] == s[end] and
                    (
                        end - start < 3 or
                        memo[start + 1][end - 1]
                    )
                ):
                    memo[start][end] = True

                    if end - start > max_right - max_left:
                        max_left, max_right = start, end

        return s[max_left:max_right + 1]