class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda word: (-len(word), word))

        for word in dictionary:
            pw = 0

            for ps in range(len(s)):
                if s[ps] == word[pw]:
                    pw += 1
                    
                    if pw == len(word):
                        return word

        return ""