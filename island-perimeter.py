class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        visited = set()

        def isLand(r, c):
            return (0 <= r < rows and
                    0 <= c < cols and
                    grid[r][c])

        def dfs(r, c):
            visited.add((r, c))

            perimeter = 0

            for x, y in directions:
                row = r + x
                col = c + y

                if (row, col) not in visited:
                    if isLand(row, col):
                        perimeter += dfs(row, col)
                    else:
                        perimeter += 1

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)
