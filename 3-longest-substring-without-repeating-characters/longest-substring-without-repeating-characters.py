class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(lambda: -1)
        p = length = 0

        for seek, char in enumerate(s):
            if p <= seen[char]:
                p = seen[char] + 1

            seen[char] = seek
            length = max(length, seek - p + 1)

        return length