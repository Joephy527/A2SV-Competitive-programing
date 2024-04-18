class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()
        perimeter = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += 4

                    for y, x in directions:
                        new_r = r + y
                        new_c = c + x

                        if (new_r, new_c) in seen:
                            perimeter -= 2

                    seen.add((r, c))

        return perimeter
