class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p2 = 0

        def checkCyclic(char1, char2):
            return (char1 == char2 or 
                    (ord(char1) + 1 - ord("a")) % 26 == ord(char2) - ord("a"))

        for p1 in range(len(str1)):
            if (p2 < len(str2) and
                checkCyclic(str1[p1], str2[p2])):
                p2 += 1

        return p2 == len(str2)
