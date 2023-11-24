class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0

        for s in range(1,len(nums)):
            if nums[s] != nums[p]:
                p += 1
                nums[p] = nums[s]

        return p + 1
