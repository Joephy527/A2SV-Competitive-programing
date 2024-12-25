class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def getGraph(size, edges):
            graph = [[] for _ in range(size)]
            
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            return graph

        def findFurthestNode(size, graph, initialVertex):
            visited = [False] * size
            visited[initialVertex] = True

            queue = deque([initialVertex])
            furthestVertex = initialVertex
            maxDistance = 0

            while queue:
                for _ in range(len(queue)):
                    vertex = queue.popleft()
                    furthestVertex = vertex

                    for neigh in graph[vertex]:
                        if not visited[neigh]:
                            visited[neigh] = True
                            queue.append(neigh)

                if queue:
                    maxDistance += 1

            return furthestVertex, maxDistance

        def findMaxDiameter(size, graph):
            initialVertex, _ = findFurthestNode(size, graph, 0)
            _, maxDistance = findFurthestNode(size, graph, initialVertex)

            return maxDistance

        n, m = len(edges1) + 1, len(edges2) + 1
        graphOne, graphTwo = getGraph(n, edges1), getGraph(m, edges2)

        diameterOne, diameterTwo = findMaxDiameter(n, graphOne), findMaxDiameter(m, graphTwo)

        return max(
                diameterOne, diameterTwo, ceil(diameterOne / 2) + ceil(diameterTwo / 2) + 1
                )
