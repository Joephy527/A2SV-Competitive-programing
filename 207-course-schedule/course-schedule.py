class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = [[] for _ in range(numCourses)]
        queue = deque()
        indegree = [0] * numCourses

        for a, b in prerequisites:
            dependencies[b].append(a)
            indegree[a] += 1

        for course in range(numCourses):
            if not indegree[course]:
                queue.append(course)

        while queue:
            course = queue.popleft()

            for dependency in dependencies[course]:
                indegree[dependency] -= 1
                if not indegree[dependency]:
                    queue.append(dependency)

        return not sum(indegree)