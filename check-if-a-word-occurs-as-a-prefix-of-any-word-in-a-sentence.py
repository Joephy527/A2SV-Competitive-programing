class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for idx, word in enumerate(words, 1):
            if word.startswith(searchWord):
                return idx

        return -1
