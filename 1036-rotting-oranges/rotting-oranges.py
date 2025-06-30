class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        minutes = fresh = 0

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        def is_fresh(row, col):
            return grid[row][col] == 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                if grid[row][col] == 1:
                    fresh += 1

        if not fresh: return 0

        while queue:
            row, col, prev_minute = queue.popleft()
            minutes = prev_minute

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and is_fresh(r, c):
                    fresh -= 1
                    grid[r][c] = 2
                    queue.append((r, c, prev_minute + 1))

        return -1 if fresh else minutes