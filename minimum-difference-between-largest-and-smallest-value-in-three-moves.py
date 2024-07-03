class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        
        nums.sort()
        minDiff = float("inf")

        for l in range(4):
            r = len(nums) - 4 + l
            minDiff = min(minDiff, nums[r] - nums[l])

        return minDiff
