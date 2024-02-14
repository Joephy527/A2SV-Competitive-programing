class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        targetCombinations = []
        subSet = []
        

        def backTrack(idx, target):
            if target <= 0:
                if target == 0:
                    targetCombinations.append(subSet[:])

                return

            prev = -1

            for i in range(idx, len(candidates)):
                if candidates[i] != prev:
                    subSet.append(candidates[i])
                    backTrack(i + 1 , target - candidates[i])
                    subSet.pop()

                prev = candidates[i]

        backTrack(0, target)

        return targetCombinations
