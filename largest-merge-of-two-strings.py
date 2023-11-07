class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        p1, p2 = 0, 0
        
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] > word2[p2]:
                res.append(word1[p1])
                p1 += 1
            elif word1[p1] < word2[p2]:
                res.append(word2[p2])
                p2 += 1
            else:
                if word1[p1:] > word2[p2:]:
                    res.append(word1[p1])
                    p1 += 1
                else:
                    res.append(word2[p2])
                    p2 += 1

        while p1 < len(word1):
            res.append(word1[p1])
            p1 += 1

        while p2 < len(word2):
            res.append(word2[p2])
            p2 += 1

        return "".join(res)
