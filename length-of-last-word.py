class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWordLength = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if lastWordLength:
                    return lastWordLength
            else:
                lastWordLength += 1

        return lastWordLength
