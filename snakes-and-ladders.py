class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)

        def helper(cell):
            r = (cell - 1) // n
            c = (cell - 1) % n
            
            if r % 2:
                c = n - 1 - c

            return [r, c]

        queue = deque([1])
        level = 0
        visited = set()

        while queue:
            level += 1

            for _ in range(len(queue)):
                cell = queue.popleft()

                for i in range(1, 7):
                    nextCell = cell + i
                    r, c = helper(nextCell)
                    
                    if board[r][c] != -1:
                        nextCell = board[r][c]
                    
                    if nextCell == n ** 2:
                        return level
                    
                    if nextCell not in visited:
                        visited.add(nextCell)
                        queue.append(nextCell)

        return -1
