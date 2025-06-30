class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        minutes = 0

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        def is_fresh(row, col):
            return grid[row][col] == 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

        while queue:
            cur = 0
            
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = row + x, col + y

                    if is_inbound(r, c) and is_fresh(r, c):
                        cur = 1
                        grid[r][c] = 2
                        queue.append((r, c))

            minutes += cur

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return minutes