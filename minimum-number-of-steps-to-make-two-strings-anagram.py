class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)

        for c in t:
            if countS[c]:
                countS[c] -= 1

        return sum(countS.values())
