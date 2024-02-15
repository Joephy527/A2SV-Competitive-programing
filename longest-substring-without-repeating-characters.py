class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterCount = defaultdict(int)
        p = maxSubString = 0

        for seek in range(len(s)):
            characterCount[s[seek]] += 1

            while characterCount[s[seek]] > 1:
                characterCount[s[p]] -= 1
                p += 1

            maxSubString = max(maxSubString, seek - p + 1)

        return maxSubString
