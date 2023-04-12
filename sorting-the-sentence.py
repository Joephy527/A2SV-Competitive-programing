class Solution:
    def sortSentence(self, s: str) -> str:
        a = list(s.split())
        b = [0] * len(a)
        for i in range(len(a)):
            b[int(a[i][-1]) - 1] = a[i][:-1]
        return " ".join(b)
