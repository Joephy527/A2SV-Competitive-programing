class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        inDegree = [0] * n
        queue = deque()
        loud = [v for v in range(n)]

        for a, b in richer:
            graph[a].append(b)
            inDegree[b] += 1

        for v in range(n):
            if not inDegree[v]:
                queue.append(v)

        while queue:
            vertex = queue.popleft()

            for neigh in graph[vertex]:
                if quiet[loud[vertex]] < quiet[loud[neigh]]:
                    loud[neigh] = loud[vertex]
                
                inDegree[neigh] -= 1

                if not inDegree[neigh]:
                    queue.append(neigh)

        return loud
