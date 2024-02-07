class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allCombinations  = []

        def backTrack(num, ref):
            if num > n:
                if len(ref) == k:
                    allCombinations.append(ref[:])
                
                return

            ref.append(num)
            backTrack(num + 1, ref)
            ref.pop()
            backTrack(num + 1, ref)

        backTrack(1, [])

        return allCombinations
