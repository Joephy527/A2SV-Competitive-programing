class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        fresh_count = minute = 0

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

                if grid[row][col] == 1:
                    fresh_count += 1

        while queue and fresh_count:
            minute += 1
            
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = row + x, col + y
                    
                    if is_inbound(r, c) and grid[r][c] == 1:
                        fresh_count -= 1
                        grid[r][c] = 2
                        queue.append((r, c))

        return -1 if fresh_count else minute