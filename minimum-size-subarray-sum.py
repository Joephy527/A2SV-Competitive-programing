class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p = targetSum = 0
        ans = len(nums) + 1
        
        for s, num in enumerate(nums):
            targetSum += num

            while targetSum >= target and p <= s:
                ans = min(ans, s - p + 1)
                targetSum -= nums[p]
                p += 1

        return 0 if ans == len(nums) + 1 else ans
