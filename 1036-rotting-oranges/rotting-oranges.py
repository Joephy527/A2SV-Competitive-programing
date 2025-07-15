class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fresh = minutes = 0
        queue = deque()

        def is_fresh(row, col):
            return (
                rows > row >= 0 <= col < cols
                and grid[row][col] == 1
            )

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        while queue and fresh:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = x + row, y + col

                    if is_fresh(r, c):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))

            minutes += 1

        return minutes if not fresh else -1