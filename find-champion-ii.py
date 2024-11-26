class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [0 for _ in range(n)]
        champion = championCount = 0

        for _, v in edges:
            graph[v] += 1

        for v in range(n):
            if not graph[v]:
                champion = v
                championCount += 1

        return champion if championCount == 1 else -1
