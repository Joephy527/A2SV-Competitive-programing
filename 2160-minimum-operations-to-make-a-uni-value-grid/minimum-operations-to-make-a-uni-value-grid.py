class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        op = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] % x != grid[0][0] % x:
                    return -1

                nums.append(grid[r][c])

        nums.sort()

        median = nums[len(nums) // 2]

        for num in nums:
            op += abs(median - num) // x

        return op