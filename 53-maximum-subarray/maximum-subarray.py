class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_sum = min(nums)

        for idx, num in enumerate(nums, 1):
            s = max(s, 0)
            s += num
            max_sum = max(max_sum, s)

        return max_sum