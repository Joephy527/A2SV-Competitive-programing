class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p1 = p2 = 0

        def checkCyclic(char1, char2):
            return (char1 == char2 or 
                    (ord(char1) + 1 - ord("a")) % 26 == ord(char2) - ord("a"))

        while p1 < len(str1) and p2 < len(str2):
            if checkCyclic(str1[p1], str2[p2]):
                p2 += 1

            p1 += 1

        return p2 == len(str2)
