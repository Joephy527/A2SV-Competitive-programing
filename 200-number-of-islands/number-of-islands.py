class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        islands = 0

        def in_bound(row, col):
            return rows > row >= 0 <= col < cols

        def is_land(row, col):
            return (
                grid[row][col] == "1" and
                not visited[row][col]
            )

        def dfs(row, col):
            visited[row][col] = True
            
            for x, y in directions:
                r, c = x + row, y + col

                if in_bound(r, c) and is_land(r, c):
                    dfs(r, c)

        for row in range(rows):
            for col in range(cols):
                if is_land(row, col):
                    dfs(row, col)
                    islands += 1

        return islands