class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        j = 0

        for num in nums:
            colors[num] += 1

        for i in range(len(nums)):
            while not colors[j]:
                j += 1

            nums[i] = j
            colors[j] -= 1