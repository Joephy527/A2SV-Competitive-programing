class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = Counter(s)

        for idx, char in enumerate(s):
            if charCount[char] == 1:
                return idx

        return -1
