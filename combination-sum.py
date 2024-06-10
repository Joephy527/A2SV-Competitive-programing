class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb, sub = [], []

        def backTrack(idx = 0, total = 0):
            if total >= target or idx == len(candidates):
                if total == target:
                    comb.append(sub[:])

                return

            sub.append(candidates[idx])
            backTrack(idx, total + candidates[idx])
            
            sub.pop()
            backTrack(idx + 1, total)

        backTrack()

        return comb
