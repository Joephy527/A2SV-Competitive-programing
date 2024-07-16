class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        maxArea = 0

        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def isLand(row, col):
            return grid[row][col] == 1

        def dfs(row, col):
            grid[row][col] = 0
            area = 1

            for x, y in directions:
                r, c = row + x, col + y

                if isInbound(r, c) and isLand(r, c):
                    area += dfs(r, c)

            return area

        for r in range(rows):
            for c in range(cols):
                if isLand(r, c):
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea
