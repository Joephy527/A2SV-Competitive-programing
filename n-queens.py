class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        distinctSolutions = []
        boardConf = [["."] * n for i in range(n)]

        col = set()
        diagonalOne = set()
        diagonalTwo = set()

        def backTrack(r):
            if r >= n:
                temp = ["".join(row) for row in boardConf]
                distinctSolutions.append(temp)

                return

            for c in range(n):
                if (c not in col
                    and r + c not in diagonalOne
                    and r - c not in diagonalTwo):

                    col.add(c)
                    diagonalOne.add(r + c)
                    diagonalTwo.add(r - c)
                    boardConf[r][c] = "Q"

                    backTrack(r + 1)

                    col.remove(c)
                    diagonalOne.remove(r + c)
                    diagonalTwo.remove(r - c)
                    boardConf[r][c] = "."

        backTrack(0)

        return distinctSolutions
