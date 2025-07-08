class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = p = 0

        for seek in range(len(s)):
            char = s[seek]

            if char in seen and p <= seen[char]:
                p = seen[char] + 1

            seen[char] = seek

            longest = max(longest, seek - p + 1)

        return longest