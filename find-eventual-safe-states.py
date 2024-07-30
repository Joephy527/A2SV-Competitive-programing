class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = {}
        safe = []

        def dfs(vertex):
            if vertex in visited:
                return visited[vertex]

            visited[vertex] = False

            for neigh in graph[vertex]:
                if not dfs(neigh):
                    return

            visited[vertex] = True

            return True

        for v in range(len(graph)):
            if dfs(v):
                safe.append(v)

        return safe
