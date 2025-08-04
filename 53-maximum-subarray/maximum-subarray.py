class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum = s = 0
        largest = float("-inf")

        for num in nums:
            s += num
            largest = max(largest, s - min_sum)
            min_sum = min(min_sum, s)

        return largest