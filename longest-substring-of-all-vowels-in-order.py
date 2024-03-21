class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        charIdxMap = {word[0]: 1}
        p = maxSubstring = 0

        for s in range(1, len(word)):
            if word[s] < word[s - 1]:
                charIdxMap.clear()
                p = s

            charIdxMap[word[s]] = s

            if len(charIdxMap) == 5:
                maxSubstring = max(maxSubstring, s - p + 1)

        return maxSubstring
