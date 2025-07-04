class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = cur_max = 0

        for num in nums:
            nxt_max = max(prev_max + num, cur_max)
            prev_max = cur_max
            cur_max = nxt_max

        return cur_max