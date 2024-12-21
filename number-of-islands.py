class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        islands = 0

        def isInbound(row, col):
            return rows > row >= 0 <= col < cols

        def isUnvisitedLand(row, col):
            return grid[row][col] == "1" and not visited[row][col]
        
        def dfs(row, col):
            visited[row][col] = True

            for x, y in directions:
                r, c = row + x, col + y

                if isInbound(r, c) and isUnvisitedLand(r, c):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if isUnvisitedLand(r, c):
                    dfs(r, c)
                    islands += 1

        return islands
