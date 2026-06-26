class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        p = max_length = 0

        for seek in range(len(s)):
            c = s[seek]
            count[c] += 1

            while count[c] > 1:
                count[s[p]] -= 1
                p += 1

            max_length = max(max_length, seek - p + 1)

        return max_length