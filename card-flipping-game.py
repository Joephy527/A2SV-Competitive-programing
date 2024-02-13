class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        singles = set(fronts + backs)

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                singles.discard(fronts[i])

        return min(singles) if singles else 0
