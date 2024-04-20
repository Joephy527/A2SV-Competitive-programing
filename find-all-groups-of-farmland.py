class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        coordinates = []

        def dfs(r, c, cur):
            if (r < 0 or r == rows or c < 0 or c == cols or
                not land[r][c] or (r, c) in seen):
                return
            
            seen.add((r, c))

            cur[0] = min(cur[0], r)
            cur[1] = min(cur[1], c)
            cur[2] = max(cur[2], r)
            cur[3] = max(cur[3], c)

            for y, x in directions:
                newR = r + y
                newC = c + x

                dfs(newR, newC, cur)

        for row in range(rows):
            for col in range(cols):
                if land[row][col] and (row, col) not in seen:
                    cur = [row, col, row, col]
                    dfs(row, col, cur)
                    coordinates.append(cur)

        return coordinates
