class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [0, 1, -1]
        prev = matrix[0]

        for r in range(1, rows):
            cur = [float("inf")] * cols

            for c in range(cols):
                if c < cols - 1:
                    cur[c] = min(cur[c], prev[c + 1])
                
                if c > 0:
                    cur[c] = min(cur[c], prev[c - 1])

                cur[c] = matrix[r][c] + min(cur[c], prev[c])

            prev = cur

        return min(prev)