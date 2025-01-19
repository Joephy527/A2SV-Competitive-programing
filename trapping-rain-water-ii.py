class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heap = []
        max_height = trapped = 0

        def is_inbound(row, col):
            return rows > row >= 0 <= col < cols

        def push_to_heap(row, col):
            heappush(heap, (heightMap[r][c], r, c))
            heightMap[r][c] = -1
        
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    push_to_heap(r, c)

        while heap:
            height, row, col = heappop(heap)
            max_height = max(max_height, height)
            trapped += max_height - height

            for x, y in directions:
                r, c = row + x, col + y

                if is_inbound(r, c) and heightMap[r][c] != -1:
                    push_to_heap(r, c)

        return trapped
