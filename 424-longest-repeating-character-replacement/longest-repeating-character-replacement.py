class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_val = 0
        longest = p = 0

        for seek in range(len(s)):
            count[s[seek]] += 1
            max_val = max(max_val, count[s[seek]])

            while (seek - p + 1) - max_val > k:
                count[s[p]] -= 1
                p += 1

            longest = max(longest, seek - p + 1)

        return longest