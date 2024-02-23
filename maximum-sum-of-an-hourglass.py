class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxHour = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 0), (1, -1), (1, 0), (1, 1)]

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                hour = 0

                for i, j in directions:
                    r, c = row + i, col + j
                    hour += grid[r][c]

                maxHour = max(maxHour, hour)

        return maxHour
