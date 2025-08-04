class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        largest = float("-inf")

        for num in nums:
            s = max(s, 0)
            s += num
            largest = max(largest, s)

        return largest