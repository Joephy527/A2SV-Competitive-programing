class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = nums[0]
        max_triplet = 0

        for i in range(len(nums) - 1):
            if nums[i] > max_i:
                max_i = nums[i]
                continue

            max_j = nums[i + 1]

            for j in range(i + 2, len(nums)):
                max_j = max(max_j, nums[j])

            max_triplet = max(
                max_triplet,
                (max_i - nums[i]) * max_j
            )

        return max_triplet