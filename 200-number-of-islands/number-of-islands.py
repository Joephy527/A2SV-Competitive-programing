class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = 0

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        def is_land(row, col):
            return grid[row][col] == "1"

        def dfs(row, col):
            grid[row][col] = "0"

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and is_land(r, c):
                    dfs(r, c)

        for row in range(rows):
            for col in range(cols):
                if is_land(row, col):
                    dfs(row, col)
                    islands += 1

        return islands