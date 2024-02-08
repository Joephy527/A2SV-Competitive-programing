class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        subset = []

        def backTrack(idx):
            if idx >= len(nums):
                allSubsets.append(subset[:])
                return

            subset.append(nums[idx])
            backTrack(idx + 1)

            subset.pop()
            backTrack(idx + 1)

        backTrack(0)
        
        return allSubsets
