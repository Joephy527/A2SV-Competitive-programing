class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        start, finish = set(), set()

        def isInBound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def canOverflow(row, col, prev):
            return heights[row][col] >= prev

        def dfs(row, col, visited, prevHeight):
            for x, y in directions:
                r, c = row + x, col + y

                if (isInBound(r, c) and (r, c) not in visited
                    and canOverflow(r, c, prevHeight)):
                    visited.add((r, c))
                    dfs(r, c, visited, heights[r][c])

        for r in range(rows):
            start.add((r, 0))
            finish.add((r, cols - 1))

            dfs(r, 0, start, heights[r][0])
            dfs(r, cols - 1, finish, heights[r][cols - 1])

        for c in range(cols):
            start.add((0, c))
            finish.add((rows - 1, c))

            dfs(0, c, start, heights[0][c])
            dfs(rows - 1, c, finish, heights[rows - 1][c])

        return list(start.intersection(finish))
