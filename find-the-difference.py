class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = Counter(s)
        countT = Counter(t)

        for char in countT:
            if countT[char] != countS[char]:
                return char
