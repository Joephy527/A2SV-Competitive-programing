class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_sum = float("-inf")

        for num in nums:
            s += num
            max_sum = max(max_sum, s)
            s = max(s, 0)

        return max_sum