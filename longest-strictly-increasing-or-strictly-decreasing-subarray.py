class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur_inc = cur_dec = longest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_inc += 1
                cur_dec = 1
            elif nums[i] < nums[i - 1]:
                cur_dec += 1
                cur_inc = 1
            else:
                cur_inc = cur_dec = 1

            longest = max(longest, cur_inc, cur_dec)

        return longest
