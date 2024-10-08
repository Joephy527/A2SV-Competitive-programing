class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [[0] * (i + 1) for i in range(query_row + 1)]
        memo[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                if memo[i][j] > 1:
                    extra = (memo[i][j] - 1) / 2.0

                    memo[i + 1][j] += extra
                    memo[i + 1][j + 1] += extra

        return min(1, memo[query_row][query_glass])
