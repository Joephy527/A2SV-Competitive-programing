class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        idx = patches = 0

        while miss <= n:
            if idx < len(nums) and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                miss += miss
                patches += 1

        return patches
