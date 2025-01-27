class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        pre_graph = {}
        answer = [False] * len(queries)

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(vertex):
            if vertex not in pre_graph:
                pre_graph[vertex] = set()

                for neigh in graph[vertex]:
                    pre_graph[vertex].update(dfs(neigh))

                pre_graph[vertex].add(vertex)

            return pre_graph[vertex]

        for course in range(numCourses):
            dfs(course)

        for idx, (pre, course) in enumerate(queries):
            answer[idx] = course in pre_graph[pre]

        return answer
