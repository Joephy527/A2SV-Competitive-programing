class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = max_i = dif = 0

        for num in nums:
            max_triplet = max(max_triplet, dif * num)
            dif = max(dif, max_i - num)
            max_i = max(max_i, num)

        return max_triplet