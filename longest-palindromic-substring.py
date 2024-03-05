class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        maxSubstring = s[0]

        for i in range(len(s) - 1):
            oneCenter = self.findPalindrome(s, i, i)
            twoCenter = self.findPalindrome(s, i, i + 1)

            if len(oneCenter) > len(maxSubstring):
                maxSubstring = oneCenter

            if len(twoCenter) > len(maxSubstring):
                maxSubstring = twoCenter

        return maxSubstring

    def findPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
