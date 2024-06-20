class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        islands = 0
        
        def isInBound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def isLand(row, col):
            return grid[row][col] == "1"
        
        def dfs(row, col):
            visited.add((row, col))

            for x, y in directions:
                r = row + x
                c = col + y

                if isInBound(r, c) and isLand(r, c) and (r, c) not in visited:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if isLand(r, c) and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands
