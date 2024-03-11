class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakPoint = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                breakPoint = i
                
                break

        if breakPoint == -1:
            nums.reverse()
            
            return

        for i in range(len(nums) - 1, breakPoint - 1, -1):
            if nums[i] > nums[breakPoint]:
                nums[i], nums[breakPoint] = nums[breakPoint], nums[i]

                break

        nums[breakPoint + 1:] = nums[len(nums) - 1:breakPoint:-1]
