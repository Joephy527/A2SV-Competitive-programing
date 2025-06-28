class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [-1] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(vertex):
            if visited[vertex] == 1:
                return False

            visited[vertex] = 1

            for neigh in graph[vertex]:
                if visited[neigh] and not dfs(neigh):
                    return False

            visited[vertex] = 0

            return True

        for course in range(numCourses):
            if visited[course] and not dfs(course):
                return False

        return True