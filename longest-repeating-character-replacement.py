class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characterCount = defaultdict(int)
        p = maxVal = 0

        for seek in range(len(s)):
            characterCount[s[seek]] += 1
            maxVal = max(maxVal, characterCount[s[seek]])

            if (seek - p + 1) - maxVal > k:
                characterCount[s[p]] -= 1
                p += 1

        return seek - p + 1
