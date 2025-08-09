class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        prev = grid[0]

        for r in range(1, rows):
            cur = [float("inf")] * cols

            for c in range(cols):
                if c < cols - 1:
                    cur[c] = min(cur[c], min(prev[c + 1:]))
                
                if c > 0:
                    cur[c] = min(cur[c], min(prev[:c]))

                cur[c] += grid[r][c]

            prev = cur

        return min(prev)