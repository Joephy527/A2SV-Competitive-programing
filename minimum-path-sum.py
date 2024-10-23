class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        memo = [[0] * m for _ in range(n)]
        memo[0][0] = grid[0][0]
        
        for j in range(1, m):
            memo[0][j] = memo[0][j - 1] + grid[0][j]
        
        for i in range(1, n):
            memo[i][0] = memo[i - 1][0] + grid[i][0]
        
        for i in range(1, n):
            for j in range(1, m):
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + grid[i][j]
        
        return memo[-1][-1]
