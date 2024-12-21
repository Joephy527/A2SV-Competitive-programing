class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0] * n
        
        def dfs(vertex, color):
            for neigh in graph[vertex]:
                if not visited[neigh]:
                    visited[neigh] = -color
                    
                    if not dfs(neigh, -color):
                        return
                elif visited[neigh] == color:
                    return

            return True

        for v in range(n):
            if not visited[v] and not dfs(v, 1):
                return False

        return True
