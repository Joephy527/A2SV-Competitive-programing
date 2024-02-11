class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0

        for s in range(len(nums)):
            if nums[s] != val:
                nums[p] = nums[s]
                p += 1

        return p
