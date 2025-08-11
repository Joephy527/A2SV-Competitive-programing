class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        pascal = [[1]]

        for row in range(1, numRows):
            cur = [1] * (row + 1)

            for i in range(1, row):
                cur[i] = pascal[-1][i] + pascal[-1][i - 1]

            pascal.append(cur)

        return pascal