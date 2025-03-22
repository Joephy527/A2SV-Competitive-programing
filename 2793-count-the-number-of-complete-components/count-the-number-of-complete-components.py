class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        connected = 0

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(vertex):
            components.append(vertex)

            for neigh in graph[vertex]:
                if not visited[neigh]:
                    visited[neigh] = True
                    dfs(neigh)

        for v in range(n):
            if not visited[v]:
                components = []
                is_connected = True

                visited[v] = True
                dfs(v)

                for comp in components:
                    if len(graph[comp]) != len(components) - 1:
                        is_connected = False
                
                connected += is_connected

        return connected