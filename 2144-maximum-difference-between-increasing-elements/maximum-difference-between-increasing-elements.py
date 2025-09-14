class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        cur_min = float("inf")
        max_dif = 0

        for num in nums:
            cur_min = min(cur_min, num)
            max_dif = max(max_dif, num - cur_min)

        return max_dif if max_dif else -1