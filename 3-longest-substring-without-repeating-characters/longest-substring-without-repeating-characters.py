class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        p = longest = 0

        for seek in range(len(s)):
            count[s[seek]] += 1

            while count[s[seek]] > 1:
                count[s[p]] -= 1
                p += 1

            longest = max(
                longest,
                seek - p + 1
            )

        return longest