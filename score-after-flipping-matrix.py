class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        res = (1 << (c - 1)) * r

        for j in range(1, c):
            val = 1 << (c - 1 - j)
            setCount = 0

            for i in range(r):
                if grid[i][j] == grid[i][0]:
                    setCount += 1

            res += max(setCount, r - setCount) * val

        return res
