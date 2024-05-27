class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)

        for idx, num in enumerate(nums):
            if (len(nums) - idx <= num and
                (idx == 0 or nums[idx - 1] < len(nums) - idx)):
                return len(nums) - idx

        return -1
