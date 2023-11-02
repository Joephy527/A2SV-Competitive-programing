class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        p = 0

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            size = i - p + 1

            if (size - max(count.values())) > k:
                count[s[p]] -= 1
                p += 1

        return i - p + 1
