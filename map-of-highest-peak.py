class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        heights = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    heights[r][c] = 0
                    queue.append((r, c))

        def isValid(row, col):
            return 0 <= row < rows and 0 <= col < cols and not isWater[row][col]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = row + x, col + y

                    if isValid(r, c) and heights[r][c] == -1:
                        heights[r][c] = heights[row][col] + 1
                        queue.append((r, c))

        return heights
