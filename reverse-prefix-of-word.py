class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                pre = word[:i + 1]
                
                return pre[::-1] + word[i + 1:]

        return word
