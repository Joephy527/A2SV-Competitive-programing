class Solution:
    def makeGood(self, s: str) -> str:
        goodString = []

        for i in range(len(s)):
            if (goodString and goodString[-1] != s[i] and
                goodString[-1].lower() == s[i].lower()):
                goodString.pop()
            else:
                goodString.append(s[i])

        return "".join(goodString)
