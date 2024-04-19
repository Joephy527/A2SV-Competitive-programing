class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        islands = 0

        def dfs(row, col):
            seen.add((row, col))

            for y, x in directions:
                newR = row + y
                newC = col + x

                if (0 <= newR < rows and 0 <= newC < cols and
                    (newR, newC) not in seen and
                    grid[newR][newC] == "1"):
                    dfs(newR, newC)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    islands += 1
                    
                    dfs(r, c)
                    
        return islands
