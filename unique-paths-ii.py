class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        memo[0][0] = 1

        for i in range(1, rows):
            memo[i][0] = memo[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        
        for j in range(1, cols):
            memo[0][j] = memo[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
                else:
                    memo[i][j] = 0
        
        return memo[rows - 1][cols - 1]
