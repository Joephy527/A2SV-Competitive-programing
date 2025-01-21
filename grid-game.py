class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row_one = sum(grid[0])
        row_two = 0
        points = float("inf")
        
        for turn_index in range(len(grid[0])):
            row_one -= grid[0][turn_index]
            points = min(points, max(row_one, row_two))
            row_two += grid[1][turn_index]
        
        return points
