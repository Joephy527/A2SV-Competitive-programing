class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backTrack(idx, add):
            if idx == len(nums):
                return add

            return (backTrack(idx + 1, add ^ nums[idx]) +
                    backTrack(idx + 1, add ))

        return backTrack(0, 0)
