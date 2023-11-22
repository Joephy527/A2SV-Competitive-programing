class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        p = ans = 0

        for seek in range(len(s)):
            if s[seek] in seen and p <= seen[s[seek]]:
                p = seen[s[seek]] + 1
            
            seen[s[seek]] = seek
            ans = max(ans, seek - p + 1)

        return ans
