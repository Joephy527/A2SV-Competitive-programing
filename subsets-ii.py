class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subSets = []
        subSet = []

        def backTrack(idx):
            if idx >= len(nums):
                subSets.append(subSet[:])

                return

            subSet.append(nums[idx])
            backTrack(idx + 1)

            subSet.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            backTrack(idx + 1)

        backTrack(0)

        return subSets
