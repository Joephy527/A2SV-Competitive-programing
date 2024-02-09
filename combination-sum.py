class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTrack(idx = 0, total = 0):
            if idx >= len(candidates) or total > target: 
                return

            if total == target:
                subSets.append(subSet[:])
                
                return

            subSet.append(candidates[idx])
            backTrack(idx, total + candidates[idx])

            subSet.pop()
            backTrack(idx + 1, total)

        subSets = []
        subSet = []

        backTrack()

        return subSets
