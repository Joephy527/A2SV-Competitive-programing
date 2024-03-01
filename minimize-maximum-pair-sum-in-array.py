class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxPair = 0

        for i in range(n // 2):
            pair = nums[i] + nums[n - i - 1]
            maxPair = max(maxPair, pair)

        return maxPair
