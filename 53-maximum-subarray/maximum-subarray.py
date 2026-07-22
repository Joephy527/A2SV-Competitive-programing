class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        max_sum = nums[0]

        for num in nums:
            cur = max(num, num + cur)
            max_sum = max(max_sum, cur)

        return max_sum