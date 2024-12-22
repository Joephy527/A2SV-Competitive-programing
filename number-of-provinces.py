class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        def dfs(vertex):
            visited[vertex] = True

            for city, connected in enumerate(isConnected[vertex]):
                if not visited[city] and connected:
                    dfs(city)

        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces
