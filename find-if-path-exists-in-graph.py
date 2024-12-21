class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(vertex):
            visited[vertex] = True

            for neigh in graph[vertex]:
                if not visited[neigh] and dfs(neigh):
                    return True

            return vertex == destination

        return dfs(source)
