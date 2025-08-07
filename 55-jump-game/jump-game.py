class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0

        for i in range(len(nums)):
            if far < i:
                break

            far = max(far, i + nums[i])

            if far >= len(nums) - 1:
                return True

        return False