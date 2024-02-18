class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def backTrack(row, col, idx):
            if idx == len(word): return True

            if (row >= m or col >= n or
                row < 0 or col < 0 or
                word[idx] != board[row][col] or
                (row, col) in visited):
                
                return False

            visited.add((row, col))
            hasWord =  (backTrack(row + 1, col, idx + 1) or
                        backTrack(row - 1, col, idx + 1) or
                        backTrack(row, col + 1, idx + 1) or
                        backTrack(row, col - 1, idx + 1))
            visited.remove((row, col))

            return hasWord

        for row in range(m):
            for col in range(n):
                if backTrack(row, col, 0):
                    return True
