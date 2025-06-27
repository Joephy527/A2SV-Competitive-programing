class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        s = sum(nums)

        def back_track(idx, target):
            if idx == len(nums):
                return target == 0

            key = (idx, target)

            if key not in memo:
                memo[key] = (
                    back_track(idx + 1, target) or 
                    back_track(idx + 1, target - nums[idx])
                ) 

            return memo[key] 

        return not s % 2 and back_track(0, s / 2)