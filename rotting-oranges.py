class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        queue = deque()
        freshCount = minutes = 0

        def isFresh(row, col):
            return (0 <= row < rows and 0 <= col < cols and
                    grid[row][col] == 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1

        while queue:
            if not freshCount: return minutes

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = row + x, col + y

                    if isFresh(r, c):
                        grid[r][c] = 2
                        freshCount -= 1
                        queue.append((r, c))

            minutes += 1

        return minutes if not freshCount else -1
