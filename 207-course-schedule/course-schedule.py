class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(course):
            visited[course] = -1

            for c in graph[course]:
                if visited[c] == 1:
                    continue

                if visited[c] == -1 or not dfs(c):
                    return False
            
            visited[course] = 1
            
            return True

        for course in range(numCourses):
            if not visited[course] and not dfs(course):
                return False

        return True