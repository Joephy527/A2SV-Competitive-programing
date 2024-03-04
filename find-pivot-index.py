class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        prefix = 0

        for idx, num in enumerate(nums):
            if prefix == s - prefix - num:
                return idx

            prefix += num

        return -1
