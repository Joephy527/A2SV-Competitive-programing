class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        shortestPaths = []

        for i in range(n - 1):
            graph[i].append(i + 1)

        def bfs():
            queue = deque([(0, 0)])
            visited = [False] * n
            visited[0] = True

            while queue:
                vertex, level = queue.popleft()

                if vertex == n - 1:
                    return level

                for city in graph[vertex]:
                    if not visited[city]:
                        visited[city] = True
                        queue.append((city, level + 1))

        for u, v in queries:
            graph[u].append(v)
            path = bfs()

            shortestPaths.append(path)

        return shortestPaths
