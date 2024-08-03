class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replacment = 0

        for i in range(len(nums) - 1, 0, -1):
            cur = nums[i]
            prev = nums[i - 1]

            if cur < prev:
                parts = ceil(prev / cur)
                nums[i - 1] = prev // parts

                replacment += parts - 1
            
        return replacment
