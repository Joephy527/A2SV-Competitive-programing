class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = splits = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            splits += left_sum >= right_sum

        return splits
