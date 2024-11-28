class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(0, 0, 0)])
        memo = [[-1] * cols for _ in range(rows)]
        memo[0][0] = 0

        def isInbound(row, col):
            return rows > row >= 0 <= col < cols

        while queue:
            obstacles, row, col = queue.popleft()

            for x, y in directions:
                r, c = row + x, col + y

                if isInbound(r, c) and memo[r][c] == -1:
                    if grid[r][c]:
                        memo[r][c] = obstacles + 1
                        queue.append((obstacles + 1, r, c))
                    else:
                        memo[r][c] = obstacles
                        queue.appendleft((obstacles, r, c))

        return memo[rows - 1][cols - 1]
