class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(vertex):
            visited[vertex] = 1

            for neigh in graph[vertex]:
                if visited[neigh] == 2:
                    continue
                elif visited[neigh] == 1 or not dfs(neigh):
                    return

            visited[vertex] = 2

            return True

        for v in range(numCourses):
            if not visited[v] and not dfs(v):
                return

        return True
