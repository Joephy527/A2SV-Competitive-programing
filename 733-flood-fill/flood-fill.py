class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        starting = image[sr][sc]

        def is_valid(row, col):
            return (
                rows > row >= 0 <= col < cols and
                image[row][col] == starting
            )

        def dfs(row, col):
            image[row][col] = color

            for x, y in directions:
                r, c = row + x, col + y
                if is_valid(r, c):
                    dfs(r, c)
        
        if starting != color:
            dfs(sr, sc)

        return image