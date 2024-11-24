class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        maxSum = negCount = 0
        minNeg = float("inf")

        for row in matrix:
            for val in row:
                maxSum += abs(val)
                minNeg = min(minNeg, abs(val))

                if val < 0:
                    negCount += 1

        if negCount % 2:
            maxSum -= 2 * minNeg

        return maxSum
