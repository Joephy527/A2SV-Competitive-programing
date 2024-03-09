class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nonDecreasing = set()
        subSequences = []

        def backTrack(idx):
            if idx >= len(nums):
                if len(subSequences) > 1:
                    nonDecreasing.add(tuple(subSequences))

                return

            if not subSequences or nums[idx] >= subSequences[-1]:
                subSequences.append(nums[idx])
                backTrack(idx + 1)
                subSequences.pop()

            backTrack(idx + 1)

        backTrack(0)

        return list(nonDecreasing)
