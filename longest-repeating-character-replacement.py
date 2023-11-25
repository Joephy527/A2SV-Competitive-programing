class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        p = ans = 0

        for seek in range(len(s)):
            count[s[seek]] += 1

            while seek - p + 1 - max(count.values()) > k:
                count[s[p]] -= 1
                p += 1

            ans = max(ans, seek - p + 1)

        return ans
