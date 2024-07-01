class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if not mat[r][c]:
                    queue.append((r, c))

        def isValidOne(row, col):
            return 0 <= row < rows and 0 <= col < cols and mat[row][col]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                distance = mat[row][col] + 1

                for x, y in directions:
                    r = row + x
                    c = col + y

                    if isValidOne(r, c) and (r, c) not in visited:
                        mat[r][c] = distance
                        visited.add((r, c))
                        queue.append((r, c))

        return mat
