class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        memo[-1][-1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m - 1:
                    memo[row][col] += memo[row + 1][col]

                if col < n - 1:
                    memo[row][col] += memo[row][col + 1]

        return memo[0][0]