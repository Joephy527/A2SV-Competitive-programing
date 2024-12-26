class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def backTrack(idx, total):
            if idx >= len(nums):
                return 1 if total == target else 0

            if (idx, total) not in memo:
                memo[(idx, total)] = (
                    backTrack(idx + 1, total + nums[idx])
                    +
                    backTrack(idx + 1, total - nums[idx])
                )

            return memo[(idx, total)]

        return backTrack(0, 0)
