class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                l, r = 0, cols - 1

                while l <= r:
                    m = l + (r - l) // 2

                    if matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        return True

                return False

        return False