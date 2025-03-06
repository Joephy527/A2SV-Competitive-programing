class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        size = len(grid) * len(grid)
        seen = [0] * (size + 1)
        a = grid_sum = 0

        for row in grid:
            for num in row:
                if seen[num]:
                    a = num
                else:
                    grid_sum += num
                    seen[num] = 1

        expected_sum = (size * (size + 1)) // 2
        b = expected_sum - grid_sum

        return [a, b]
