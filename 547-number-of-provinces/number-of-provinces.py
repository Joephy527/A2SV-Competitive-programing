class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(vertex):
            for neigh, connected in enumerate(isConnected[vertex]):
                if connected and not visited[neigh]:
                    visited[neigh] = True
                    dfs(neigh)

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces += 1

        return provinces