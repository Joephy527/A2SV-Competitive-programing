class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        queue = deque([(0, -1)])
        visited = set()
        pathLength = 0
        shortestPaths = [-1] * n

        for u, v in redEdges:
            graph[u].append((v, 1))

        for u, v in blueEdges:
            graph[u].append((v, 0))

        while queue:
            for _ in range(len(queue)):
                vertex, vertexColor = queue.popleft()

                if shortestPaths[vertex] == -1:
                    shortestPaths[vertex] = pathLength

                for neigh, color in graph[vertex]:
                    if (neigh, color) not in visited and color != vertexColor:
                        visited.add((neigh, color))
                        queue.append((neigh, color))

            pathLength += 1

        return shortestPaths
