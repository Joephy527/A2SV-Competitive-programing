class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[0] * cols for _ in range(rows)]
        island_area = {}
        island_number = 1
        island = 0

        def in_bound(row, col):
            return rows > row >= 0 <= col < cols

        def is_land(row, col):
            return grid[row][col] == 1 and not visited[row][col]

        def dfs(row, col):
            visited[row][col] = island_number

            area = 1

            for x, y in directions:
                r, c = x + row, y + col

                if in_bound(r, c) and is_land(r, c):
                    area += dfs(r, c)
            
            return area

        for row in range(rows):
            for col in range(cols):
                if is_land(row, col):
                    area = dfs(row, col)
                    island_area[island_number] = area
                    island_number += 1
                    island = max(island, area)

        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    area = 1
                    seen = set()

                    for x, y in directions:
                        r, c = x + row, y + col

                        if (
                            in_bound(r, c) and grid[r][c] and
                            visited[r][c] not in seen
                        ):
                            area += island_area[visited[r][c]]
                            seen.add(visited[r][c])

                    island = max(island, area)

        return island