class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                cur = int(board[r][c]) - 1
                box_idx = (r // 3) * 3 + (c // 3)
                b = 1 << cur

                if (
                    b & row[r] or
                    b & col[c] or
                    b & box[box_idx]
                ):
                    return False

                row[r] |= b
                col[c] |= b
                box[box_idx] |= b

        return True