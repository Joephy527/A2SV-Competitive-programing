class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_s = max_s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                max_s = max(max_s, cur_s)
                cur_s = 0
            
            cur_s += nums[i]

        return max(max_s, cur_s)
