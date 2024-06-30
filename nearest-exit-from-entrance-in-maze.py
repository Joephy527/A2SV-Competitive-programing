class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set(tuple(entrance))
        queue = deque([(entrance[0], entrance[1], 0)])

        def isValidPath(row, col):
            return (0 <= row < rows and 0 <= col < cols and
                    maze[row][col] == ".")

        def isExit(row, col):
            return ((not row or not col or row == rows - 1 or
                    col == cols - 1) and
                    [row, col] != entrance)

        while queue:
            for _ in range(len(queue)):
                row, col, level = queue.popleft()

                for x, y in directions:
                    r = row + x
                    c = col + y

                    if isValidPath(r, c) and (r, c) not in visited:
                        if isExit(r, c):
                            return level + 1

                        visited.add((r, c))
                        queue.append((r, c, level + 1))

        return -1
