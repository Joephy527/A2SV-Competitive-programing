class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        areas = defaultdict(int)
        areas[0] = 1
        islands = 2
        max_area = 1

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        def is_land(row, col):
            return grid[row][col] == 1

        def dfs(row, col):
            grid[row][col] = islands
            areas[islands] += 1

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and is_land(r, c):
                    dfs(r, c)

        def get_area(row, col):
            seen = set()
            area = 1

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and grid[r][c] > 0 and grid[r][c] not in seen:
                    seen.add(grid[r][c])
                    area += areas[grid[r][c]]

            return area

        for row in range(rows):
            for col in range(cols):
                if is_land(row, col):
                    dfs(row, col)
                    islands += 1

        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    max_area = max(max_area, get_area(row, col))

        return max(max_area, max(areas.values()))