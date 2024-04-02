class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        productArr = [[1 for _ in range(m)] for _ in range(n)]
        product = 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                productArr[r][c] = product % 12345
                product = (product * grid[r][c]) % 12345

        product = 1
        
        for r in range(len(grid) - 1, -1, - 1):
            for c in range(len(grid[0]) - 1, -1, -1):
                productArr[r][c] = (productArr[r][c] * product) % 12345
                product = (product * grid[r][c]) % 12345

        return productArr
