class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows, cols = m, n
        grid = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isInBound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def checkGuarded(row, col):
            for x, y in directions:
                r, c = row + x, col + y
                
                while isInBound(r, c) and grid[r][c] != 1:
                    grid[r][c] = 2
                    r += x
                    c += y

        for row, col in walls:
            grid[row][col] = 1

        for row, col in guards:
            grid[row][col] = 1

        for row, col in guards:
            checkGuarded(row, col)

        return sum(1 for r in range(rows) for c in range(cols) if not grid[r][c])
