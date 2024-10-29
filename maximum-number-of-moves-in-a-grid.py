class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 1), (0, 1), (1, 1)]
        memo = [[-1] * cols for _ in range(rows)]
        maxMoves = 0

        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def isBigger(cur, prev):
            return cur > prev

        def dfs(row, col, moves):
            if memo[row][col] != -1:
                return memo[row][col]

            prev = grid[row][col]
            curMaxMoves = moves

            for y, x in directions:
                r, c = y + row, x + col

                if isInbound(r, c) and isBigger(grid[r][c], prev):
                    curMaxMoves = max(curMaxMoves, dfs(r, c, moves + 1))

            memo[row][col] = curMaxMoves
            return curMaxMoves

        for r in range(rows):
            maxMoves = max(maxMoves, dfs(r, 0, 0))

        return maxMoves
