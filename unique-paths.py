class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        memo[-1][-1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r != m - 1:
                    memo[r][c] += memo[r + 1][c]

                if c != n - 1:
                    memo[r][c] += memo[r][c + 1]

        return memo[0][0]
