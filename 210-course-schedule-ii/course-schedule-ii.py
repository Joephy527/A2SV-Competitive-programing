class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [-1] * numCourses
        order = []

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(vertex):
            if visited[vertex] == 1:
                return False

            visited[vertex] = 1

            for neigh in graph[vertex]:
                if not visited[neigh]:
                    continue
                
                if not dfs(neigh):
                    return False

            visited[vertex] = 0
            order.append(vertex)

            return True

        for course in range(numCourses):
            if not visited[course]:
                continue
            
            if not dfs(course):
                return []

        return order