class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        queue = deque()
        level = -1

        def isValid(row, col):
            return 0 <= row < rows and 0 <= col < cols and not grid[row][col]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                level = grid[row][col]

                for x, y in directions:
                    r, c = row + x, col + y

                    if isValid(r, c) and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
                        grid[r][c] = grid[row][col] + 1

        return level - 1 if level > 1 else -1
