class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalOrder = []
        row = col = 0
        positiveDir = True

        while True:
            diagonalOrder.append(mat[row][col])

            if row == len(mat) - 1 and col == len(mat[0]) - 1:
                break

            if positiveDir:
                if row > 0 and col < len(mat[0]) - 1:
                    row, col = row - 1, col + 1
                elif row <= 0 and col < len(mat[0]) - 1:
                    col += 1
                    positiveDir = False
                else:
                    row += 1
                    positiveDir = False
            else:
                if col > 0 and row < len(mat) - 1:
                    row, col = row + 1, col - 1
                elif col <= 0 and row < len(mat) - 1:
                    row += 1
                    positiveDir = True
                else:
                    col += 1
                    positiveDir = True

        return diagonalOrder
