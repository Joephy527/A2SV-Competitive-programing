class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        bottom, right = len(matrix), len(matrix[0])
        spiral = []

        while top < bottom and left < right:
            for i in range(left, right):
                spiral.append(matrix[top][i])
            
            top += 1

            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            
            right -= 1

            if top >= bottom or left >= right:
                break

            for i in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom - 1][i])

            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                spiral.append(matrix[i][left])

            left += 1

        return spiral