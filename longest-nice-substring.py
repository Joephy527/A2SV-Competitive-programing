class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        chars = set(s)
        for i in range(len(s)):
            if (s[i].lower() not in chars or
                s[i].upper() not in chars):
                lns1 = self.longestNiceSubstring(s[:i])
                lns2 = self.longestNiceSubstring(s[i+1:])

                return max(lns1, lns2, key=len)

        return s
