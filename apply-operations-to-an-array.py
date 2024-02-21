class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        p = 0

        for s in range(len(nums)):
            if nums[s] != 0:
                nums[p], nums[s] = nums[s], nums[p]
                p += 1

        return nums
