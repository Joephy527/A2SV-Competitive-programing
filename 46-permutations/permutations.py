class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        permutation = []
        used = [False] * n

        def back_track():
            if len(permutation) == n:
                permutations.append(permutation[:])

                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    permutation.append(nums[i])
                    back_track()
                    permutation.pop()
                    used[i] = False

        back_track()

        return permutations