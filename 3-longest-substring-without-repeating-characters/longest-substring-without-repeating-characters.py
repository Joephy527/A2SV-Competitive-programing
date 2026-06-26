class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx_map = defaultdict(lambda: -1)
        p = max_length = 0

        for seek in range(len(s)):
            c = s[seek]
            idx = idx_map[c]

            if c in idx_map and p <= idx:
                p = idx + 1

            idx_map[c] = seek

            max_length = max(max_length, seek - p + 1)

        return max_length