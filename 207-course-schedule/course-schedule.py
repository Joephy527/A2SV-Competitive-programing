class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(vertex):
            if visited[vertex] == -1:
                return

            if visited[vertex] == 1:
                return True

            visited[vertex] = -1

            for neigh in graph[vertex]:
                if not dfs(neigh):
                    return

            visited[vertex] = 1
            return True

        for v in range(numCourses):
            if not dfs(v):
                return False

        return True