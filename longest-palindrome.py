class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        pal = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                pal += 2
            else:
                seen.add(c)

        return pal + 1 if seen else pal
