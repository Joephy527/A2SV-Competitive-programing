class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                transpose[col][row] = matrix[row][col]

        return transpose
