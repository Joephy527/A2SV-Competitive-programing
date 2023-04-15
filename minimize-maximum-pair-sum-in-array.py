class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a = 0
        for i in range(len(nums) // 2):
            a = max(a, nums[i] + nums[len(nums) - i - 1])
        return a
