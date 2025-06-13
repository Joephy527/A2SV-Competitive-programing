class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        col, row, box = (
            defaultdict(set),
            defaultdict(set),
            defaultdict(set)
        )

        for r in range(rows):
            for c in range(cols):
                cur = board[r][c]

                if cur == ".": continue

                box_idx = (r // 3, c // 3)

                if (
                    cur in col[c] or
                    cur in row[r] or
                    cur in box[box_idx]
                ):
                    return False

                col[c].add(cur)
                row[r].add(cur)
                box[box_idx].add(cur)

        return True