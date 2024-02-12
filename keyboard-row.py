class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keybordRows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        rowMap = {}
        oneRowWords = []

        for i in range(len(keybordRows)):
            for j in keybordRows[i]:
                rowMap[j] = i+1

        for word in words:
            isOneRow = True
            lowerWord = word.lower()
            row = rowMap[lowerWord[0]]

            for c in lowerWord:
                if rowMap[c] != row:
                    isOneRow = False

            if isOneRow:
                oneRowWords.append(word)

        return oneRowWords
