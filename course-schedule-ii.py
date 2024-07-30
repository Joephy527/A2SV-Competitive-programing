class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        colors = [0] * numCourses
        ordering = []

        for course, pre in prerequisites:
            graph[pre].append(course)

        def dfs(vertex):
            if colors[vertex] == 1:
                return

            colors[vertex] = 1

            for neigh in graph[vertex]:
                if not colors[neigh] == 2 and not dfs(neigh):
                    return

            colors[vertex] = 2
            ordering.append(vertex)

            return True

        for v in range(numCourses):
            if not colors[v] and not dfs(v):
                return

        ordering.reverse()

        return ordering
