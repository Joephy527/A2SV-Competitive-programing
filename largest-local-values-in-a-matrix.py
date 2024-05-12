class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxMatrix = []
        directions = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

        for r in range(1, len(grid) - 1):
            row = []
            for c in range(1, len(grid[0]) - 1):
                maxVal = grid[r][c]

                for y, x in directions:
                    newR = r + y
                    newC = c + x
                    maxVal = max(maxVal, grid[newR][newC]) 

                row.append(maxVal)

            maxMatrix.append(row)

        return maxMatrix
