class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            total |= num

        return total << (len(nums) - 1)