class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols
        
        def back_track(row, col, idx):
            if idx == len(word):
                return True

            if (not is_inbound(row, col) or
                visited[row][col] or
                word[idx] != board[row][col]):
                return

            visited[row][col] = True

            for x, y in directions:
                r, c = row + x, col + y
                
                if back_track(r, c, idx + 1):
                    return True
            
            visited[row][col] = False

        for row in range(rows):
            for col in range(cols):
                if back_track(row, col, 0):
                    return True

        return False
