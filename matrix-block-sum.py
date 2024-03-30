class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = mat[:][:]
        
        for r in range(rows):
            for c in range(cols):
                prefix[r][c] += ((prefix[r - 1][c] if r > 0 else 0) +
							    (prefix[r][c - 1] if c > 0 else 0) -
							    (prefix[r - 1][c - 1] if r > 0 and c > 0 else 0))

        res = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                res[i][j] = (prefix[min(i + k, rows - 1)][min(j + k, cols - 1)] +
                               (prefix[max(i - k - 1, 0)][max(j - k - 1, 0)] if i - k > 0 and j - k > 0 else 0) -
                               (prefix[i - k - 1][min(j + k, cols - 1)] if i - k > 0 else 0) - 
                               (prefix[min(i + k, rows - 1)][j - k - 1] if j - k > 0 else 0))  

        return res
