class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashCols = defaultdict(set)
        hashRows = defaultdict(set)
        hashGrid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue

                if (board[i][j] in hashCols[j] or 
                    board[i][j] in hashRows[i] or
                    board[i][j] in hashGrid[(i // 3, j // 3)]):
                    return False

                hashCols[j].add(board[i][j])
                hashRows[i].add(board[i][j])
                hashGrid[(i // 3, j // 3)].add(board[i][j])

        return True
