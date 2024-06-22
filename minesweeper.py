class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        rows, cols = len(board), len(board[0])
        clickRow, clickCol = click

        def isInBound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def mineCount(row, col):
            mines = 0

            for x, y in directions:
                r = row + x
                c = col + y

                if isInBound(r, c) and board[r][c] == "M":
                    mines += 1

            return mines

        def dfs(row, col):
            mines = mineCount(row, col)

            if not mines:
                board[row][col] = "B"

                for x, y in directions:
                    r = row + x
                    c = col + y

                    if isInBound(r, c) and board[r][c] == "E":
                        dfs(r, c)
            else:
                board[row][col] = str(mines)

        if board[clickRow][clickCol] == "M":
            board[clickRow][clickCol] = "X"
        else:
            dfs(clickRow, clickCol)

        return board
