class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        set_bits = p = max_nice = 0

        for s in range(len(nums)):
            while set_bits & nums[s] != 0:
                set_bits ^= nums[p]
                p += 1

            set_bits |= nums[s]

            max_nice = max(max_nice, s - p + 1)

        return max_nice