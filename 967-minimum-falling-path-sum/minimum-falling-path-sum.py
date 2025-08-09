class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prev = matrix[0]

        for r in range(1, rows):
            cur = prev[:]

            for c in range(cols):
                if c < cols - 1:
                    cur[c] = min(cur[c], prev[c + 1])
                
                if c > 0:
                    cur[c] = min(cur[c], prev[c - 1])

                cur[c] += matrix[r][c]

            prev = cur

        return min(prev)