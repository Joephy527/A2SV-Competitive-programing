class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        col, row = {}, {}
        lucky = []

        for idx, r in enumerate(matrix):
            row[idx] = min(r)

        for c in range(cols):
            mx = 0

            for r in range(rows):
                mx = max(mx, matrix[r][c])

            col[c] = mx

        for r in range(rows):
            for c in range(cols):
                cur = matrix[r][c]
                if cur == col[c] and cur == row[r]:
                    lucky.append(cur)

        return lucky
