class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = len(nums) - bisect_right(nums, 0)
        neg = bisect_left(nums, 0)
        
        return max(neg, pos)