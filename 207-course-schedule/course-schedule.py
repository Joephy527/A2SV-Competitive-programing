class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        indegree = [0] * numCourses
        queue = deque()

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for idx, num in enumerate(indegree):
            if not num:
                queue.append(idx)

        while queue:
            course = queue.popleft()
            visited[course] = True

            for c in graph[course]:
                indegree[c] -= 1

                if not indegree[c] and not visited[c]:
                    queue.append(c)

        return not sum(indegree)