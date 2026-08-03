class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        permutation = []

        def back_track(set_bits):
            if len(permutation) == n:
                permutations.append(permutation[:])

                return

            for i in range(n):
                set_bit = 1 << i

                if not set_bit & set_bits:
                    permutation.append(nums[i])
                    back_track(set_bit | set_bits)
                    permutation.pop()

        back_track(0)

        return permutations