class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        def is_inbounds(row, col):
            return rows > row >= 0 <= col < cols
        
        def bfs(start):
            queue = deque(start)
            visited = set(start)

            while queue:
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = row + x, col + y

                    if (
                        is_inbounds(r, c) and
                        (r, c) not in visited and
                        heights[r][c] >= heights[row][col]
                    ):
                        visited.add((r, c))
                        queue.append((r, c))

            return visited

        atlantics = bfs(atlantic)
        pacifics = bfs(pacific)

        return (
            [
                [r, c] for r in range(rows) for c in range(cols)
                if (r, c) in atlantics and (r, c) in pacifics
            ]
        )