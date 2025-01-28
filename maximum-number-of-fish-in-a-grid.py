class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        max_fish = 0

        def is_inbounds(row, col):
            return rows > row >= 0 <= col < cols
        
        def dfs(row, col):
            cur_fish = grid[row][col]

            for x, y in directions:
                r, c = row + x, col + y

                if (
                    is_inbounds(r, c) and 
                    not visited[r][c] and
                    grid[r][c]
                ):
                    visited[r][c] = True
                    cur_fish += dfs(r, c)

            return cur_fish

        for r in range(rows):
            for c in range(cols):
                if (
                    grid[r][c] and 
                    not visited[r][c]
                ):
                    visited[r][c] = True
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish
