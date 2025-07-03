class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        p = longest = 0

        for seek in range(len(s)):
            c = s[seek]

            if c in seen and p <= seen[c]:
                p = seen[c] + 1
            
            seen[c] = seek
            longest = max(
                longest,
                seek - p + 1
            )

        return longest