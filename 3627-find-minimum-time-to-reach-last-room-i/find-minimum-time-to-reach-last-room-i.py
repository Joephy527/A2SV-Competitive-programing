class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(0, 0, 0)]

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        while queue:
            time, row, col = heappop(queue)

            if row == rows - 1 and col == cols - 1:
                return time

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and not visited[r][c]:
                    visited[r][c] = True
                    time_to_move = max(time, moveTime[r][c]) + 1
                    heappush(queue, (time_to_move, r, c))