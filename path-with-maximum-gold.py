class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            gold = grid[r][c]
            grid[r][c] = 0
            
            maxGold = max(dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1))
            
            grid[r][c] = gold
            
            return gold + maxGold

        maxGold = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    maxGold = max(maxGold, dfs(r, c))
        
        return maxGold
