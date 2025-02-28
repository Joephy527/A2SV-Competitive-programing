class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pos = max_neg = cur_sum = 0

        for num in nums:
            cur_sum += num

            max_pos = max(max_pos, cur_sum)
            max_neg = min(max_neg, cur_sum)

        return max_pos - max_neg
