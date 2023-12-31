class Solution:
    def sortSentence(self, s: str) -> str:
        splitArr = s.split()
        finalArr = [0] * len(splitArr)
        
        for word in splitArr:
            idx = int(word[-1]) - 1
            finalArr[idx] = word[:-1]

        return " ".join(finalArr)
