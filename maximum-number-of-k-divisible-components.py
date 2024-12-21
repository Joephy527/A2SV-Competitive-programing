class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        divisible = [0]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(vertex):
            cur = values[vertex]
            visited[vertex] = True
            
            for neigh in graph[vertex]:
                if not visited[neigh]:
                    cur += dfs(neigh)
            
            if not cur % k:
                divisible[0] += 1
                
                return 0
            else:
                return cur

        dfs(0)

        return divisible[0]
