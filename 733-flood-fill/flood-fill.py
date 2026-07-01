class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        original_color = image[sr][sc]

        if original_color == color:
            return image

        image[sr][sc] = color
        queue = deque([(sr, sc)])

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols 

        while queue:
            row, col = queue.popleft()

            for x, y in directions:
                r, c = row + x, col + y
                
                if is_inbound(r, c) and image[r][c] == original_color:
                    image[r][c] = color
                    queue.append((r, c))

        return image