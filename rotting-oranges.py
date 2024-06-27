class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        freshCount = minutes = 0
        queue = deque()
        
        def isFresh(row, col):
            return 0 <= row < n and 0 <= col < m and grid[r][c] == 1
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    freshCount += 1
        
        while queue:
            if not freshCount:
                return minutes

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for x, y in directions:
                    r = row + x
                    c = col + y

                    if isFresh(r, c):
                        grid[r][c] = 2
                        freshCount -= 1
                        queue.append((r, c))
            
            minutes += 1
        

        return minutes if not freshCount else -1
