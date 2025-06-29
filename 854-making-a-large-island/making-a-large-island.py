class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        area_map = defaultdict(int)

        def in_bound(row, col):
            return rows > row >= 0 <= col < cols

        def is_land(row, col):
            return grid[row][col] == 1

        def dfs(row, col):
            grid[row][col] = -1
            area = 1

            for x, y in directions:
                r, c = x + row, y + col

                if in_bound(r, c):
                    if is_land(r, c):
                        area += dfs(r, c)
                    elif not grid[r][c]:
                        water.add((r, c))

            return area

        for row in range(rows):
            for col in range(cols):
                if is_land(row, col):
                    water = set()
                    area = dfs(row, col)

                    for cell in water:
                        area_map[cell] += area

        if area_map:
            return 1 + max(area_map.values())

        return rows * cols if grid[0][0] else 1