class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = float("inf")
        max_dif = -1

        for num in nums:
            max_dif = max(max_dif, num - min_num)
            min_num = min(min_num, num)

        return -1 if max_dif < 1 else max_dif