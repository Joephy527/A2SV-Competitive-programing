class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 2: return True

        inversion_count = nums[0] < nums[-1]

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                inversion_count += 1

        return inversion_count < 2
