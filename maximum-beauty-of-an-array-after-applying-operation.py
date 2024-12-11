class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        p = 0

        for s in range(len(nums)):
            if nums[s] - nums[p] > k * 2:
                p += 1

        return len(nums) - p
