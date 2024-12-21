class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]

        def isInbound(row, col):
            return rows > row >= 0 <= col < cols

        def isLand(row, col):
            return grid[row][col]
        
        def dfs(row, col):
            visited[row][col] = True
            perimeter = 0

            for x, y in directions:
                r, c = row + x, col + y

                if isInbound(r, c):
                    if isLand(r, c) and not visited[r][c]:
                        perimeter += dfs(r, c)
                    elif not visited[r][c]:
                        perimeter += 1
                else:
                    perimeter += 1

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)
