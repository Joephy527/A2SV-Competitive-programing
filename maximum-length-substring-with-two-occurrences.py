class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        p = maxSubArr = 0

        for seek in range(len(s)):
            count[s[seek]] += 1
            
            while count[s[seek]] > 2:
                count[s[p]] -= 1
                p += 1

            maxSubArr = max(maxSubArr, seek - p + 1)

        return maxSubArr
