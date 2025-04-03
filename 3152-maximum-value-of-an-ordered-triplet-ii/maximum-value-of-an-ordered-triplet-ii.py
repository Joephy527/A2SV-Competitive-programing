class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = max_dif = max_triplet = 0

        for num in nums:
            max_triplet = max(max_triplet, max_dif * num)
            max_dif = max(max_dif, max_i - num)
            max_i = max(max_i, num)

        return max_triplet