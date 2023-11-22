class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l = 0
        length = 0

        for i in range(len(s)):
            while s[i] in count:
                count.remove(s[l])
                l += 1

            count.add(s[i])
            length = max(length, len(count))

        return length
