class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = defaultdict(int)
        minSum = float("inf")

        def dfs(r, c):
            if r == rows:
                return 0
            
            if c >= rows or c < 0:
                return float("inf")
            
            if (r, c) in memo:
                return memo[(r, c)]

            minSum = min(
                dfs(r + 1, c - 1),
                dfs(r + 1, c),
                dfs(r + 1, c + 1)
            )
            curSum = minSum + matrix[r][c]
            memo[(r, c)] = curSum
            
            return curSum

        for col in range(cols):
            minSum = min(minSum, dfs(0, col))
        
        return minSum
