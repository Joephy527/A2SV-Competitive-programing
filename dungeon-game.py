class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        memo = [[0] * m for _ in range(n)]
        memo[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if r == n - 1 and c == m - 1:
                    continue

                cur = float("inf")
                
                if r < n - 1:
                    cur = min(cur, memo[r + 1][c])

                if c < m - 1:
                    cur = min(cur, memo[r][c + 1])

                memo[r][c] = max(1, cur - dungeon[r][c])

        return memo[0][0]
