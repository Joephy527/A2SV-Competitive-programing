class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split()
        reversedStr = []

        for string in strList:
            reversedStr.append(string[::-1])

        return " ".join(reversedStr)
