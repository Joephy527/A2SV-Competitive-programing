class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubArray = float("inf")
        p = minSum = 0

        for s in range(len(nums)):
            minSum += nums[s]

            while minSum >= target:
                minSubArray = min(minSubArray, s - p + 1)
                minSum -= nums[p]
                p += 1

        return minSubArray if minSubArray != float("inf") else 0
