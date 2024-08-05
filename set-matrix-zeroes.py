class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row, col = set(), set()

        def isZero(r, c):
            return r in row or c in col and (matrix[r][c])

        for r in range(rows):
            for c in range(cols):
                if not matrix[r][c]:
                    row.add(r)
                    col.add(c)

        for r in range(rows):
            for c in range(cols):
                if isZero(r, c):
                    matrix[r][c] = 0
