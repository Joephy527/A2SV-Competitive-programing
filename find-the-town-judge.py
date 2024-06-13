class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1: return -1

        inDegree = [0] * (n + 1)
        outDegree = [0] * (n + 1)
        
        for a, b in trust:
            inDegree[b] += 1
            outDegree[a] += 1

        for i in range(1, n + 1):
            if inDegree[i] == n - 1 and outDegree[i] == 0:
                return i

        return -1
