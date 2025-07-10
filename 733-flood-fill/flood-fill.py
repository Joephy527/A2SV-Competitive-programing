class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            rows, cols = len(image), len(image[0])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            original = image[sr][sc]

            def is_inbound(row, col):
                return rows > row >= 0 <= col < cols

            def is_not_visited(row, col):
                return image[row][col] == original

            def dfs(row, col):
                image[row][col] = color

                for x, y in directions:
                    r, c = row + x, col + y

                    if is_inbound(r, c) and is_not_visited(r, c):
                        dfs(r, c)

            dfs(sr, sc)

        return image