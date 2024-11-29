class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        minHeap = [(0, 0, 0)]

        def isInbound(row, col):
            return rows > row >= 0 <= col < cols

        while minHeap:
            time, row, col = heappop(minHeap)

            if (row, col) == (rows - 1, cols - 1):
                return time

            for x, y in directions:
                r, c = row + x, col + y

                if isInbound(r, c) and not visited[r][c]:
                    wait = 0 if abs(grid[r][c] - time) % 2 else 1
                    t = max(grid[r][c] + wait, time + 1)

                    heappush(minHeap, (t, r, c))
                    visited[r][c] = True
