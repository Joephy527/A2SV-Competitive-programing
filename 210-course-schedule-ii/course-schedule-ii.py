class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()
        order = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for idx, num in enumerate(indegree):
            if not num:
                queue.append(idx)

        while queue:
            course = queue.popleft()
            order.append(course)

            for c in graph[course]:
                indegree[c] -= 1

                if not indegree[c]:
                    queue.append(c)

        return order if len(order) == numCourses else []