class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        distinctSolutions = []
        board = [["."] * n for i in range(n)]
        column, additionDiagonal, substractDiagonal = set(), set(), set()

        def backTrack(row):
            if row >= n:
                solution = ["".join(row) for row in board]
                distinctSolutions.append(solution)

                return

            for col in range(n):
                if (col not in column and row + col not in additionDiagonal
                    and row - col not in substractDiagonal):

                    column.add(col)
                    additionDiagonal.add(row + col)
                    substractDiagonal.add(row - col)
                    board[row][col] = "Q"

                    backTrack(row + 1)

                    column.remove(col)
                    additionDiagonal.remove(row + col)
                    substractDiagonal.remove(row - col)
                    board[row][col] = "."

        backTrack(0)

        return distinctSolutions
