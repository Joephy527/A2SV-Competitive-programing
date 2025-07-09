class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1 , 0)]
        spiral = []

        def is_valid(row, col):
            return (
                rows > row >= 0 <= col < cols and
                not visited[row][col]
            )

        def get_spiral(row, col, d, t):
            if not visited[row][col]:
                spiral.append(matrix[row][col])
                visited[row][col] = True

            x, y = directions[d]
            r, c = row + x, col + y
            
            if is_valid(r, c):
                get_spiral(r, c, d, 0)
            else:
                if t >= 4: return
                get_spiral(row, col, (d + 1) % 4, t + 1)

        get_spiral(0, 0, 0, 0)
        return spiral