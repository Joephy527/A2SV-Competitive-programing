class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols
        
        def dfs(row, col):
            area = 1

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and grid[r][c]:
                    grid[r][c] = 0
                    area += dfs(r, c)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    grid[r][c] = 0
                    max_area = max(max_area, dfs(r, c))

        return max_area